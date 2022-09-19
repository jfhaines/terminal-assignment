import json
import pokebase as pb

# pokemon list
pokemon = {}
for i in range(1, 151):
    pokemon_info = pb.pokemon(i)
    name = str(pokemon_info.name)
    hp = str(pokemon_info.__dict__['stats'][0].__dict__['base_stat'])
    attack = str(pokemon_info.__dict__['stats'][1].__dict__['base_stat'])
    defense = str(pokemon_info.__dict__['stats'][2].__dict__['base_stat'])
    moves_list = pokemon_info.__dict__['moves']
    moves_name_list = []
    for move in moves_list:
        moves_name_list.append((str(move.__dict__['move'])))
        pokemon[name] = {'hp': hp, 'attack': attack, 'defense': defense, 'moves': moves_name_list}

json_string = json.dumps(pokemon)

with open('pokemon-info.json', 'w') as f:
    f.write(json_string)

# print(str(pb.pokemon(1).__dict__['stats'][0].__dict__['base_stat']))


# moves list
moves = {}
for i in range(1, 827):
    move_info = pb.move(i).__dict__
    moves[move_info['name']] = {'power': move_info['power'], 'pp': move_info['pp']}

json_moves = json.dumps(moves)

with open('moves-info.json', 'w') as f:
    f.write(json_moves)