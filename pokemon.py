from math import remainder
from import_json import pokemon_data, move_data
from random import randint, uniform
from moves import Move
import pokebase as pb


def get_moves(num, pokemon):
    moves = {}
    number_of_available_moves = len(pokemon['info']['moves'])

    while len(moves.keys()) < num:
        rand_num = randint(0, number_of_available_moves - 1)
        move_name = pokemon['info']['moves'][rand_num]
        if move_name in move_data.keys() and move_name not in moves.keys():
            move_details = move_data[move_name]
            moves[move_name] = move_details

    return moves



class Pokemon:
    @classmethod
    def __get_random_pokemon_name(cls):
        rand_num = randint(0, len(pokemon_data.keys()) - 1)
        return list(pokemon_data.keys())[rand_num]

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
    
    def use_move(self, move, defending_pokemon):
        damage = (((((((2 * 20/5 + 2) * self.attack * move.power) / defending_pokemon.defense) / 50) + 2) * randint(217, 255)) / 255)
        defending_pokemon.remaining_hp = 0 if damage > defending_pokemon.remaining_hp else defending_pokemon.remaining_hp - damage
        move.remaining_pp -= 1
        print(damage)



p1 = Pokemon.generate()
p2 = Pokemon.generate()
move = p1.moves[list(p1.moves.keys())[0]]

p1.use_move(move, p2)

print(p1.name, p1.attack, move.power, p2.name, p2.defense)
print(p2.hp, p2.remaining_hp)