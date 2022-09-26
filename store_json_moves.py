import json

import pokebase as pb

# moves list
def get_move_info():
    moves = {}
    for i in range(1, 827):
        move_info = pb.move(i)
        if isinstance(move_info.power, int):
            moves[move_info.name] = {'power': move_info.power, 'pp': move_info.pp}
    return moves


json_moves = json.dumps(get_move_info())
with open('moves-info.json', 'w') as f:
    f.write(json_moves)