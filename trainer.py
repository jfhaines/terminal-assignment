from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb
from item import PokeBall, HealthPotion, MovePotion, Item

class ItemBag:
    def __init__(self):
        self.__pokeballs = PokeBallContainer()
        self.__health_potions = HealthPotionContainer()
        self.__move_potions = MovePotionContainer()
    
    def __repr__(self):
        return f'{self.pokeballs.type.name}: {self.pokeballs.count} remaining, {self.health_potions.type.name}: {self.health_potions.count} remaining & {self.move_potions.type.name}: {self.move_potions.count} remaining'

    @property
    def pokeballs(self):
        return self.__pokeballs
    
    @property
    def health_potions(self):
        return self.__health_potions
    
    @property
    def move_potions(self):
        return self.__move_potions
    
    def pickup(self, item):
        if isinstance(item, PokeBall):
            self.pokeballs.add(item)
        
        elif isinstance(item, HealthPotion):
            self.health_potions.add(item)
        
        elif isinstance(item, MovePotion):
            self.move_potions.add(item)
    
    @property
    def available(self):
        available = []
        if not self.pokeballs.is_empty:
            available.append(self.pokeballs)

        if not self.health_potions.is_empty:
            available.append(self.health_potions)

        if not self.move_potions.is_empty:
            available.append(self.move_potions)
        return available
    
    @property
    def available_str(self):
        list_store = list(enumerate(self.available))
        for index, item in list_store:
            list_store[index] = f'{index} = {item}'
        return ', '.join(list_store)


class Container:
    def __init__(self, type):
        self.__collection = []
        self.__type = type
    
    def __repr__(self):
        return f"{self.type()} ({self.count} remaining)"
    
    @property
    def collection(self):
        return self.__collection

    @property
    def type(self):
        return self.__type
    
    def use(self, pokemon):
        self.get.use(pokemon)
        self.collection.pop()

    @property
    def count(self):
        return len(self.collection)
    
    def add(self, item):
        if isinstance(item, self.type):
            self.collection.append(item)
    
    @property
    def get(self):
        return self.collection[0] if not self.is_empty else None
    
    @property
    def is_empty(self):
        return True if self.count == 0 else False



class PokeBallContainer(Container):
    def __init__(self):
        super().__init__(PokeBall)
    
    def use(self, pokemon, player, map, item_position):
        self.get.use(pokemon, player, map, item_position)
        self.collection.pop()

class HealthPotionContainer(Container):
    def __init__(self):
        super().__init__(HealthPotion)

class MovePotionContainer(Container):
    def __init__(self):
        super().__init__(MovePotion)




class PokemonCollection():
    def __init__(self):
        self.__collection = []
    
    def add(self, pokemon):
        self.__collection.append(pokemon)
    
    @property
    def available(self):
        available = []
        for pokemon in self.__collection:
            if pokemon.remaining_hp > 0:
                available.append(pokemon)
        print(available)
        return available
    
    @property
    def available_str(self):
        list_store = list(enumerate(self.available))
        for index, pokemon in list_store:
            list_store[index] = f"{index} = {pokemon}"
        return ', '.join(list_store)

    @property
    def all(self):
        return self.__collection

    def switch(self, index):
        pokemon = self.__collection[index]
        self.__collection.pop(index)
        self.__collection.insert(0, pokemon)
    
    @property
    def active(self):
        return self.__collection[0]


    

class Trainer:
    def __init__(self, name, pokemon):
        self.__name = name
        self.__pokemon = pokemon
        self.__display_str = '!'
    
    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # pokemon
    @property
    def pokemon(self):
        return self.__pokemon
    
    @pokemon.setter
    def pokemon(self, pokemon):
        self.__pokemon = pokemon
    
    # display string
    @property
    def display_str(self):
        return self.__display_str
    
    @display_str.setter
    def display_str(self, display_str):
        self.__display_str = display_str



class NpcTrainer(Trainer):
    @classmethod
    def __generate_random_pokemon_list(cls, num):
        pokemon_list = PokemonCollection()
        for i in range(num):
            pokemon_list.add(Pokemon.generate())
        return pokemon_list

    @classmethod
    def generate(cls):
        return cls(names.get_first_name(), cls.__generate_random_pokemon_list(randint(1, 3)))


class Player(Trainer):
    @classmethod
    def generate(cls):
        return cls('Joe', [0, 0], PokemonCollection(), ItemBag())

    def __init__(self, name, position, pokemon, items):
        super().__init__(name, pokemon)
        self.__items = items
        self.__position = position
        self.display_str = '@'
    
    # items
    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, items):
        self.__items = items

    # position
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
    
    
    def pickup_item(self, item, map, item_position):
        self.items.pickup(item)
        map.set(item_position, None)
    
    def __attack_opponent(self, my_pokemon, opponent_pokemon):
        move_index = int(input(f"Use which move? {my_pokemon.available_moves_str}: "))
        my_pokemon.use_move(my_pokemon.available_moves[move_index], opponent_pokemon)
    
    def __get_attacked(self, my_pokemon, opponent_pokemon):
        rand_index = randint(0, len(opponent_pokemon.available_moves) - 1)
        opponent_pokemon.use_move(opponent_pokemon.available_moves[rand_index], my_pokemon)
        
    def switch_pokemon(self):
        index = int(input(f"Which Pokemon do you want to use? {self.pokemon.available_str}: "))
        self.pokemon.switch(index)
        print(f"Switched to {self.pokemon.active.name}.")

    def __use_item(self, my_pokemon, opponent_pokemon = None, map = None, pokemon_position = None):
        is_catchable = bool(opponent_pokemon)
        while True:
            if len(self.items.available) == 0:
                print('No available items')
                break
            if not is_catchable and len(self.items.available) == 1 and self.items.available[0].type == PokeBall:
                print('No available items.')
                break
            item_index = int(input(f"Which item to use? {self.items.available_str}: "))
            item_type = self.items.available[item_index]
            if item_type.type == PokeBall and not is_catchable:
                print("Can't use a Poke Ball on a Trainer's Pokemon.")
                continue
            else:
                if item_type.type == PokeBall:
                    item_type.use(opponent_pokemon, self, map, pokemon_position)
                else:
                    item_type.use(my_pokemon)
                print(f'Used {item_type.type.name}.')
                print(self.items)
                break


    def pokemon_battle(self, opponent_pokemon, map = None, pokemon_position = None):
        my_pokemon = self.pokemon.active
        is_catchable = bool(map)
        print(f'Your selected pokemon is {my_pokemon.name}. You are facing {opponent_pokemon.name}.')
        while True:
            my_pokemon = self.pokemon.active

            option = int(input('What action to take? (0 = Use move, 1 = Use item, 2 = Switch Pokemon: '))
            if option == 1:
                if is_catchable:
                    self.__use_item(my_pokemon, opponent_pokemon, map, pokemon_position)
                    continue
                else:
                    self.__use_item(my_pokemon)
                    continue
            elif option == 2:
                self.switch_pokemon()
                continue
            

            self.__attack_opponent(my_pokemon, opponent_pokemon)

            if opponent_pokemon.remaining_hp == 0:
                print(f'{my_pokemon.name} beat {opponent_pokemon.name}.')
                return True
        
            self.__get_attacked(my_pokemon, opponent_pokemon)

            if my_pokemon.remaining_hp == 0:
                print(f'{opponent_pokemon.name} beat {my_pokemon.name}.')
                return False



    def move(self, map):
        direction = input('What direction do you want to move? (l = Left, r = Right, u = Up, d = Down: ')

        if direction == 'l':
            new_position = [self.position[0], self.position[1] - 1]
        
        elif direction == 'r':
            new_position = [self.position[0], self.position[1] + 1]
        
        elif direction == 'u':
            new_position = [self.position[0] - 1, self.position[1]]

        elif direction == 'd':
            new_position = [self.position[0] + 1, self.position[1]]
        
        adj_square = map.get(new_position)

        if isinstance(adj_square.current_value, Item):
            self.pickup_item(adj_square.current_value, map, new_position)
        
        elif isinstance(adj_square.current_value, NpcTrainer):
            pass



    # battle trainer
    # pokemon fight
    # switch pokemon
    # use move
    # use potion
    # use pokeball

    # move
