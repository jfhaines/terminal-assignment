import json
import sys

import pokebase as pb

arg = sys.argv[1]

if arg.isdigit():
    arg = int(arg)
else:
    sys.exit("Invalid argument: Has to be an integer above 0 and below 905.")

pokemon_index = arg

# pokemon list
def get_pokemon_info():
    pokemon = {}
    for i in range(1, pokemon_index):
        pokemon_info = pb.pokemon(i)
        name = pokemon_info.name
        hp = pokemon_info.stats[0].base_stat
        attack = pokemon_info.stats[1].base_stat
        defense = pokemon_info.stats[2].base_stat
        moves_list = pokemon_info.moves
        moves_name_list = []
        for move in moves_list:
            moves_name_list.append((str(move.move)))
        pokemon[name] = {'hp': hp, 'attack': attack, 'defense': defense, 'moves': moves_name_list}
    return pokemon



# store JSON data
json_pokemon = json.dumps(get_pokemon_info())
with open('pokemon-info.json', 'w') as f:
    f.write(json_pokemon)
