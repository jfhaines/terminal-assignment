from moves import move_list
from random import randint, uniform

class Pokemon:
    pokemon_prototypes = {
        'Pikachu': {'health_range': [40, 80], 'attack_range': [1, 1.5], 'appearance_likelihood': 5, 'type': 'Electric'},
        'Charizard': {'health_range': [80, 130], 'attack_range': [2, 3], 'appearance_likelihood': 3, 'type': 'Fire'},
        'Blastoise': {'health_range': [80, 130], 'attack_range': [2, 3], 'appearance_likelihood': 2, 'type': 'Water'},
        'Mew': {'health_range': [250, 450], 'attack_range': [4, 5], 'appearance_likelihood': 1, 'type': 'Psychic'},
        'Sceptile': {'health_range': [70, 120], 'attack_range': [1.5, 2.5], 'appearance_likelihood': 2, 'type': 'Grass'},
        'Gyarados': {'health_range': [100, 160], 'attack_range': [3, 3.5], 'appearance_likelihood': 2, 'type': 'Psychic'},
        'Bulbasaur': {'health_range': [40, 80], 'attack_range': [0.5, 1.5], 'appearance_likelihood': 6, 'type': 'Grass'},
        'Typhlosion': {'health_range': [70, 110], 'attack_range': [2, 3], 'appearance_likelihood': 2, 'type': 'Fire'},
        'Growlithe': {'health_range': [40, 80], 'attack_range': [1, 2], 'appearance_likelihood': 3, 'type': 'Fire'}
    }

    @classmethod
    def __generate_random_pokemon_name(cls):
        pokemon_pool = []
        for pokemon_name, info in cls.pokemon_prototypes.items():
            for i in range(info['appearance_likelihood']):
                pokemon_pool.append(pokemon_name)
        rand_num = randint(0, len(pokemon_pool) - 1)
        pokemon = pokemon_pool[rand_num]
        return pokemon
    
    @classmethod
    def __generate_random_health(cls, pokemon_name):
        pokemon = cls.pokemon_prototypes[pokemon_name]
        health = randint(pokemon['health_range'][0], pokemon['health_range'][1])
        return health
    
    @classmethod
    def __generate_random_attack(cls, pokemon_name):
        pokemon = cls.pokemon_prototypes[pokemon_name]
        attack = round(uniform(pokemon['attack_range'][0], pokemon['attack_range'][1]) * 2) / 2
        return attack

    @classmethod
    def __generate_random_moves(cls, pokemon_name):
        pokemon = cls.pokemon_prototypes[pokemon_name]
        move_options = []
        for move in move_list:
            if move.type == pokemon['type'] or move.type == 'Standard':
                move_options.append(move)
        move1 = move_options[randint(0, len(move_options)) - 1]
        while True:
            move2 = move_options[randint(0, len(move_options)) - 1]
            if move2 == move1:
                continue
            else: 
                break
        return [move1, move2]

    @classmethod
    def generate(cls):
        pokemon_name = cls.__generate_random_pokemon_name()
        health = cls.__generate_random_health(pokemon_name)
        attack = cls.__generate_random_attack(pokemon_name)
        moves = cls.__generate_random_moves(pokemon_name)
        return cls(pokemon_name, health, attack, moves)

    def __init__(self, name, total_health, attack, move_list):
        self.name = name
        self.total_health = total_health
        self.remaining_health = total_health
        self.attack = attack
        self.move_list = move_list