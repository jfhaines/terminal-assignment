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

# print((charmander.__dict__.keys()))
print((charmander.moves[0].__dict__['move']))

print(pb.move(9).__dict__['name'])

print(pb.pokemon(850))