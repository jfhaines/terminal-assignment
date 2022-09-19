import json
from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb

class Trainer:
    def __init__(self, name, pokemon_list):
        self.name = name
        self.pokemon_list = pokemon_list


class NPC_Trainer(Trainer):
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
    pass

pokemon = pokedex.get(dex=1)

charmander = pb.pokemon('charmander')


# stats
# print(charmander.__dict__['stats'][5].__dict__['base_stat'])

# extract moves list
# moves_list = []
# for i in charmander.moves:
#     moves_list.append(i.__dict__['move'].name)

# move details
# for i in range(len(moves_list)):
#     info = pb.move(moves_list[i]).__dict__
#     move = {'name': info['name'], 'power': info['power'], 'pp': info['pp']}
#     moves_list[i] = move

# print(moves_list)


# 826 moves


# print(pb.move(moves_list[0]).__dict__['pp'])

# print(pb.move(9).__dict__['name'])







with open('pokemon-info.json', 'r') as f:
    info = f.read()
    print(json.loads(info)['bulbasaur']['hp'])

# loop through all moves, get key stats