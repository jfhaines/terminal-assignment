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
        self.name = name
        self.hp = hp
        self.remaining_hp = hp
        self.attack = attack
        self.defense = defense
        self.moves = moves

print(Pokemon.generate().__dict__)