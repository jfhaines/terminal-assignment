import json
import pokebase as pb

# pokemon list
def get_pokemon_info():
    pokemon = {}
    for i in range(1, 151):
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


# moves list
def get_move_info():
    moves = {}
    for i in range(1, 827):
        move_info = pb.move(i)
        if isinstance(move_info.power, int):
            moves[move_info.name] = {'power': move_info.power, 'pp': move_info.pp}
    return moves



# store JSON data
json_pokemon = json.dumps(get_pokemon_info())
with open('pokemon-info.json', 'w') as f:
    f.write(json_pokemon)


json_moves = json.dumps(get_move_info())
with open('moves-info.json', 'w') as f:
    f.write(json_moves)