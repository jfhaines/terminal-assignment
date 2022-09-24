from math import remainder
from import_json import pokemon_data, move_data
from random import randint, uniform
from moves import Move
import pokebase as pb
from custom_exceptions import InputError
from utility import get_index
from utility import rand_unique_items


class Pokemon:
    @classmethod
    def generate(cls):
        pokemon_name = rand_unique_items(1, pokemon_data.keys())
        stats = pokemon_data[pokemon_name]
        return cls(name = pokemon_name, hp = stats['hp'], attack = stats['attack'], defense = stats['defense'], moves = rand_unique_items(4, pokemon_data[pokemon_name]['moves']))
    
    def __repr__(self):
        return f"{' '.join(self.name.split('-')).capitalize()} (HP: {self.remaining_hp}/{self.hp}, Attack: {self.attack}, Defense: {self.defense})"

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
    
    
    def use_move(self, opponent_pokemon, attacking_pokemon_is_npc=False):
        if attacking_pokemon_is_npc:
            move_index = randint(0, len(opponent_pokemon.available_moves) - 1)
        else:
            while True:
                try:
                    move_index = get_index(f"Use which move? {self.available_moves_str}: ", self.available_moves)
                    break
                except InputError as err:
                    print(err.user_message)
        move = self.available_moves[move_index]
        damage = int((((((((2 * 20/5 + 2) * self.attack * move.power) / opponent_pokemon.defense) / 50) + 2) * randint(217, 255)) / 255))
        opponent_pokemon.remaining_hp = 0 if damage > opponent_pokemon.remaining_hp else opponent_pokemon.remaining_hp - damage
        move.remaining_pp -= 1
        print (f"{self.name} used {move.name} dealing {damage} damage. {opponent_pokemon.name} has {opponent_pokemon.remaining_hp}/{opponent_pokemon.hp} hp remaining.")

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