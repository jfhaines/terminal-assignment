from contextlib import AsyncExitStack
from import_json import pokemon_data, move_data
from random import randint


class Move:
    @classmethod
    def generate(cls, num, pokemon_name):
        moves = []
        used_indexes = []
        number_of_available_moves = len(pokemon_data[pokemon_name]['moves'])

        while len(moves) < num:
            while True:
                rand_num = randint(0, number_of_available_moves - 1)
                if rand_num not in used_indexes:
                    break
            
            move_name = pokemon_data[pokemon_name]['moves'][rand_num]
            if move_name in move_data.keys(): 
                power = move_data[move_name]['power']
                pp = move_data[move_name]['pp']
                moves.append(cls(move_name, power, pp))
        
        return moves

    def __init__(self, name, power, pp):
        self.name = name
        self.power = power
        self.pp = pp
        self.remaining_pp = pp

    def __repr__(self):
        return f'Move(name: {self.name}, power: {self.power}, pp: {self.pp}, remaining_pp: {self.remaining_pp})'


# move_list = [
#     Move('Thunderbolt', 'Electric', 20, 3),
#     Move('Volt Tackle', 'Electric', 11, 15),
#     Move('Shock Wave', 'Electric', 15, 6),
#     Move('Flamethrower', 'Fire', 22, 4),
#     Move('Fire Blast', 'Fire', 15, 7),
#     Move('Flame Burst', 'Fire', 12, 12),
#     Move('Hydro Pump', 'Water', 22, 4),
#     Move('Water Pulse', 'Water', 15, 7),
#     Move('Water Gun', 'Water', 12, 12),
#     Move('Waterfall', 'Water', 19, 6),
#     Move('Leaf Blade', 'Grass', 12, 12),
#     Move('Giga Drain', 'Grass', 15, 7),
#     Move('Leaf Storm', 'Grass', 22, 4),
#     Move('Confusion', 'Psychic', 15, 7),
#     Move('Cosmic Power', 'Psychic', 24, 3),
#     Move('Psybeam', 'Psychic', 15, 6),
#     Move('Hyperbeam', 'Standard', 25, 3),
#     Move('Quick Attack', 'Standard', 13, 9),
#     Move('Tackle', 'Standard', 10, 17),
#     Move('Take Down', 'Standard', 11, 10),
#     Move('Crunch', 'Standard', 15, 9)
# ]