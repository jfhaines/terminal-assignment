from pokemon import Pokemon
from random import randint
import names
import pypokedex as pokedex
import pokebase as pb

class Trainer:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon_list = pokemon


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
        return cls(input('What is your player name? '), [0, 0], [], {'poke_balls': {}, 'health_potions': {}, 'move_potions': {}})

    def __init__(self, name, position, pokemon, items):
        super().__init__(name, pokemon)
        self.items = items
        self.position = position