from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb
from item import PokeBall, HealthPotion, MovePotion, Item
from custom_exceptions import InputError
from utility import get_index


class ItemBag:
    def __init__(self):
        self.__pokeballs = PokeBallContainer()
        self.__health_potions = HealthPotionContainer()
        self.__move_potions = MovePotionContainer()
    
    def __repr__(self):
        return f'{self.pokeballs.type.name}: {self.pokeballs.count} remaining, {self.health_potions.type.name}: {self.health_potions.count} remaining, {self.move_potions.type.name}: {self.move_potions.count} remaining'

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
    
    def use(self, pokemon, player):
        caught = self.get.use(pokemon, player)
        self.collection.pop()
        if caught == True:
            return True
        else:
            return False

class HealthPotionContainer(Container):
    def __init__(self):
        super().__init__(HealthPotion)

class MovePotionContainer(Container):
    def __init__(self):
        super().__init__(MovePotion)




class PokemonCollection():
    def __init__(self):
        self.__collection = []
    
    def __repr__(self):
        pokemon_list = []
        for pokemon in self.__collection:
            pokemon_list.append(str(pokemon))
        return f"{', '.join(pokemon_list)}"
    
    def add(self, pokemon):
        self.__collection.append(pokemon)
    
    @property
    def available(self):
        available = []
        for pokemon in self.__collection:
            if pokemon.remaining_hp > 0:
                available.append(pokemon)
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
        pokemon = self.available[index]
        self.__collection.remove(pokemon)
        self.__collection.insert(0, pokemon)
    
    @property
    def active(self):
        return self.available[0]
    
    @property
    def count_available(self):
        return len(self.available)


    

class Trainer:
    def __init__(self, name, pokemon):
        self.__name = name
        self.__pokemon = pokemon
        self.__display_str = '!'
    
    def __repr__(self):
        return self.name

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
        self.pokemon.add(Pokemon.generate())
    
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
        while True:
            try:
                user_input = input('Do you want to pickup {item.name}? (y | n) ')
                if user_input == 'n':
                    return
                elif user_input == 'y':
                    self.items.pickup(item)
                    map.set(item_position, None)
                    print(f'You picked up {item.name}. Item bag: {self.items}.')
                    return
                else:
                    raise InputError(user_input)

            except InputError as err:
                print(err.user_message)
    
    
    def __get_attacked(self, my_pokemon, opponent_pokemon):
        rand_index = randint(0, len(opponent_pokemon.available_moves) - 1)
        opponent_pokemon.use_move(opponent_pokemon.available_moves[rand_index], my_pokemon)
        
    def switch_pokemon(self):
        while True:
            try:
                index = get_index(f"Which Pokemon do you want to use? {self.pokemon.available_str}: ", self.pokemon.available)
            except InputError as err:
                print(err.user_message)
            else:
                self.pokemon.switch(index)
                print(f"Switched to {self.pokemon.active.name}.")
                break

    def __use_item(self, my_pokemon, opponent_pokemon = None):
        is_catchable = bool(opponent_pokemon)
        while True:
            if len(self.items.available) == 0:
                print('No available items')
                return
            if not is_catchable and len(self.items.available) == 1 and self.items.available[0].type == PokeBall:
                print('No available items.')
                return
            try:
                item_index = get_index(f"Which item to use? {self.items.available_str}: ", self.items.available)
            except InputError as err:
                print(err.user_message)
            else:
                item_type = self.items.available[item_index]

                if item_type.type == PokeBall and not is_catchable:
                    print("Can't use a Poke Ball on a Trainer's Pokemon.")
                    continue
                else:
                    if item_type.type == PokeBall:
                        caught = item_type.use(opponent_pokemon, self)
                    else:
                        item_type.use(my_pokemon)
                        caught = False
                    print(f'Used {item_type.type.name}.')
                    print(self.items)
                    return caught


    def pokemon_battle(self, opponent_pokemon, is_catchable):
        my_pokemon = self.pokemon.active
        print(f'Your selected pokemon is {my_pokemon}. You are facing {opponent_pokemon}.')
        while True:
            my_pokemon = self.pokemon.active
            option = input('What action to take? (0 = Use move, 1 = Use item, 2 = Switch Pokemon, 3 = Exit battle, 4 = Show items, 5 = Show Pokemon: ')
            try:
                if option == '0':
                    my_pokemon.use_move(opponent_pokemon)

                    if opponent_pokemon.remaining_hp == 0:
                        print(f'{my_pokemon.name} beat {opponent_pokemon.name}.')
                        return 'Won'
            
                    self.__get_attacked(my_pokemon, opponent_pokemon)

                    if my_pokemon.remaining_hp == 0:
                        print(f'{opponent_pokemon.name} beat {my_pokemon.name}.')
                        return 'Lost'

                elif option == '1':
                    if is_catchable:
                        caught = self.__use_item(my_pokemon, opponent_pokemon)
                        if caught == True:
                            return 'Exit'
                        else:
                            continue
                    else:
                        self.__use_item(my_pokemon)
                        continue

                elif option == '2':
                    self.switch_pokemon()
                    continue

                elif option == '3':
                    return 'Exit'

                elif option == '4':
                    print(self.items)
                    continue

                elif option == '5':
                    print(self.pokemon)
                    continue

                else:
                    raise InputError(option)

            except InputError as err:
                print(err.user_message)


    def trainer_battle(self, trainer):
        while True:
            try:
                user_input = input(f'Would you like to battle Pokemon Trainer {trainer.name}? (y | n): ')
                if user_input == 'n':
                    return
                elif user_input == 'y':
                    pass
                else:
                    raise InputError(user_input)
            except InputError as err:
                print(err.user_message)
            else:
                if self.pokemon.count_available == 0:
                    print("You don't have any available Pokemon. You can't battle.")
                    return
                elif trainer.pokemon.count_available == 0:
                    print(f"Pokemon Trainer {trainer.name} has no available Pokemon. You can't battle.")
                    return
                while True:
                    result = self.pokemon_battle(trainer.pokemon.active, False)
                    if result == 'Exit':
                        return 'Exit'

                    if self.pokemon.count_available == 0:
                        print(f'You have been defeated by {trainer.name}. You have no available Pokemon left.')
                        return 'Lost'
                    
                    if trainer.pokemon.count_available == 0:
                        print(f'You have won against {trainer.name}. They have no Pokemon remaining.')
                        return 'Won'

    def __change_square(self, map, new_position):
        map.set(new_position, self)
        map.set(self.position, None if not isinstance(map.get(self.position).former_val, Pokemon) else Pokemon.generate())
        self.position = new_position


    def move(self, map):
        while True:
            try:
                action = input('What do you want to do? (a = Move Left, d = Move Right, w = Move Up, s = Move Down, i = Show Items, p = Show Pokemon: ')

                if action == 'i':
                    print(self.items)
                    map.display()
                    continue

                elif action == 'p':
                    print(self.pokemon)
                    map.display()
                    continue

                elif action == 'a':
                    new_position = [self.position[0], self.position[1] - 1]
                
                elif action == 'd':
                    new_position = [self.position[0], self.position[1] + 1]
                
                elif action == 'w':
                    new_position = [self.position[0] - 1, self.position[1]]

                elif action == 's':
                    new_position = [self.position[0] + 1, self.position[1]]

                else:
                    raise InputError(action)

            except InputError as err:
                print(err.user_message)
                map.display()
            else:
                adj_square = map.get(new_position)

                if isinstance(adj_square.current_val, Item):
                    self.pickup_item(adj_square.current_val, map, new_position)
                
                elif isinstance(adj_square.current_val, Pokemon):
                    self.__change_square(map, new_position)
                    map.display()
                    rand_num = randint(1, 3)
                    if rand_num == 1:
                        print(f'A wild {map.get(self.position).former_val} appeared.')
                        self.pokemon_battle(map.get(self.position).former_val, True)
                    else:
                        continue
                
                elif isinstance(adj_square.current_val, NpcTrainer):
                    if self.trainer_battle(adj_square.current_val) == 'Won':
                        map.set(new_position, None)
                
                elif adj_square.current_val == None:
                    self.__change_square(map, new_position)

                map.display()
            