from math import remainder
from import_json import pokemon_data, move_data
from random import randint, uniform
from moves import Move
import pokebase as pb
from custom_exceptions import InputError
from utility import get_index


class Pokemon:
    @classmethod
    def __get_random_pokemon_name(cls):
        rand_num = randint(0, len(pokemon_data.keys()) - 1)
        return list(pokemon_data.keys())[rand_num]
    
    def __repr__(self):
        return f"{' '.join(self.name.split('-')).capitalize()} (HP: {self.remaining_hp}/{self.hp}, Attack: {self.attack}, Defense: {self.defense})"

    @classmethod
    def generate(cls):
        pokemon_name = cls.__get_random_pokemon_name()
        stats = pokemon_data[pokemon_name]
        return cls(name = pokemon_name, hp = stats['hp'], attack = stats['attack'], defense = stats['defense'], moves = Move.generate(4, pokemon_name))

    def __init__(self, name, hp, attack, defense, moves):
        self.__name = name
        self.__hp = hp
        self.__remaining_hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__moves = moves
        self.__display_str = '*'

    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # hp
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__hp = hp
    
    # remaining_hp
    @property
    def remaining_hp(self):
        return self.__remaining_hp
    
    @remaining_hp.setter
    def remaining_hp(self, remaining_hp):
        self.__remaining_hp = remaining_hp
    
    # attack
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self, attack):
        self.__attack = attack
    
    # defense
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, defense):
        self.__defense = defense
    
    # moves
    @property
    def moves(self):
        return self.__moves
    
    @moves.setter
    def moves(self, moves):
        self.__moves = moves

    # display string
    @property
    def display_str(self):
        return self.__display_str
    
    @display_str.setter
    def display_str(self, display_str):
        self.__display_str = display_str
    
    
    def use_move(self, defending_pokemon):
        while True:
            try:
                move_index = get_index(f"Use which move? {self.available_moves_str}: ", self.available_moves)
            except InputError as err:
                print(err.user_message)
            else:
                move = self.available_moves[move_index]
                damage = int((((((((2 * 20/5 + 2) * self.attack * move.power) / defending_pokemon.defense) / 50) + 2) * randint(217, 255)) / 255))
                defending_pokemon.remaining_hp = 0 if damage > defending_pokemon.remaining_hp else defending_pokemon.remaining_hp - damage
                move.remaining_pp -= 1
                print (f"{self.name} used {move.name} dealing {damage} damage. {defending_pokemon.name} has {defending_pokemon.remaining_hp}/{defending_pokemon.hp} hp remaining.")
                break

    @property
    def available_moves(self):
        available = []
        for move in self.moves:
            if move.remaining_pp > 0:
                available.append(move)
        return available
    
    @property
    def available_moves_str(self):
        list_store = list(enumerate(self.available_moves))
        for index, move in list_store:
            list_store[index] = f'{index} = {move}'
        return ', '.join(list_store)