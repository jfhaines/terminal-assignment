from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb
from item import PokeBall, HealthPotion, MovePotion, Item
from custom_exceptions import InputError
from utility import get_index
from bag import ItemBag, Container, PokemonCollection


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

    def pokemon_battle(self, opponent_pokemon, is_catchable):
        print(f'Your selected pokemon is {self.pokemon.active}. You are facing {opponent_pokemon}.')
        while True:
            my_pokemon = self.pokemon.active
            option = input('What action to take? (0 = Use move, 1 = Use item, 2 = Switch Pokemon, 3 = Exit battle, 4 = Show items, 5 = Show Pokemon: ')
            try:
                if option == '0':
                    my_pokemon.use_move(opponent_pokemon)

                    if opponent_pokemon.remaining_hp == 0:
                        print(f'{my_pokemon.name} beat {opponent_pokemon.name}.')
                        return 'Won'
            
                    opponent_pokemon.use_move(my_pokemon, True)

                    if my_pokemon.remaining_hp == 0:
                        print(f'{opponent_pokemon.name} beat {my_pokemon.name}.')
                        return 'Lost'

                elif option == '1':
                    if is_catchable:
                        caught = self.items.use(my_pokemon, opponent_pokemon)
                        if caught == True:
                            return 'Exit'
                        else:
                            continue
                    else:
                        self.items.use(my_pokemon)
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
            