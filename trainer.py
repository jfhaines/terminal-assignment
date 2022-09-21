from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb
from item import PokeBall, HealthPotion, MovePotion, Item


class Trainer:
    def __init__(self, name, pokemon):
        self.__name = name
        self.__pokemon_list = pokemon
        self.__display_str = '!'
    
    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # pokemon list
    @property
    def pokemon_list(self):
        return self.__pokemon_list
    
    @pokemon_list.setter
    def pokemon_list(self, pokemon_list):
        self.__pokemon_list = pokemon_list
    
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
        pokemon_list = []
        for i in range(num):
            pokemon_list.append(Pokemon.generate())
        return pokemon_list

    @classmethod
    def generate(cls):
        return cls(names.get_first_name(), cls.__generate_random_pokemon_list(randint(1, 3)))


class Player(Trainer):
    @classmethod
    def generate(cls):
        return cls('Joe', [0, 0], [], {})

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
        self.items[item.name] = 1 if item.name not in self.items else self.items[item.name] + 1
        map.set(item_position, None)
    
    def __your_turn(self, my_pokemon, opponent_pokemon):
        my_pokemon_available_moves = []
        for move in my_pokemon.moves:
            if move.remaining_pp > 0:
                my_pokemon_available_moves.append(move)
        move_index = int(input(f"Use which move? {('0 = ' + my_pokemon_available_moves[0].name) if len(my_pokemon_available_moves) >= 1 else ''}{(', 1 = ' + my_pokemon_available_moves[1].name) if len(my_pokemon_available_moves) >= 2 else ''}{(', 2 = ' + my_pokemon_available_moves[2].name) if len(my_pokemon_available_moves) >= 3 else ''}{(', 3 = ' + my_pokemon_available_moves[3].name) if len(my_pokemon_available_moves) >= 4 else ''} "))
        my_pokemon.use_move(my_pokemon_available_moves[move_index], opponent_pokemon)
    
    def __opponent_turn(self, my_pokemon, opponent_pokemon):
        opponent_pokemon_available_moves = []
        for move in opponent_pokemon.moves:
            if move.remaining_pp > 0:
                opponent_pokemon_available_moves.append(move)
        opponent_number_of_moves = len(opponent_pokemon_available_moves)
        rand_index = randint(0, opponent_number_of_moves - 1)
        opponent_pokemon.use_move(opponent_pokemon_available_moves[rand_index], my_pokemon)

    def __use_item(self, pokemon):
        item_list = self.items.enumerate()
        input

    def pokemon_battle(self, my_pokemon, opponent_pokemon):
        print(f'Your selected pokemon is {my_pokemon.name}. You are facing {opponent_pokemon.name}.')
        while True:
            self.__your_turn(my_pokemon, opponent_pokemon)

            if opponent_pokemon.remaining_hp == 0:
                print(f'{my_pokemon.name} beat {opponent_pokemon.name}.')
                return True
            
            self.__opponent_turn(my_pokemon, opponent_pokemon)

            if my_pokemon.remaining_hp == 0:
                print(f'{opponent_pokemon.name} beat {my_pokemon.name}.')
                return False



    def move(self, map):
        direction = input('What direction do you want to move? (l = Left, r = Right, u = Up, d = Down')

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
