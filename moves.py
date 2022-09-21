from contextlib import AsyncExitStack
from import_json import pokemon_data, move_data
from random import randint


class Move:
    @classmethod
    def generate(cls, num, pokemon_name):
        available_moves = []
        for move in pokemon_data[pokemon_name]['moves']:
            if move in move_data:
                available_moves.append(move)
        
        indexes = []
        while len(indexes) < min(num, len(available_moves)):
            rand_num = randint(0, min(num, len(available_moves) - 1))
            if rand_num not in indexes:
                indexes.append(rand_num)
        
        moves = []
        for index in indexes:
            move_name = available_moves[index]
            move_power = move_data[move_name]['power']
            move_pp = move_data[move_name]['pp']
            moves.append(cls(move_name, move_power, move_pp))
        
        return moves

    def __init__(self, name, power, pp):
        self.__name = name
        self.__power = power
        self.__pp = pp
        self.__remaining_pp = pp

    def __repr__(self):
        return f'Move(name: {self.name}, power: {self.power}, pp: {self.pp}, remaining_pp: {self.remaining_pp})'

    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # power
    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        self.__power = power
    
    # pp
    @property
    def pp(self):
        return self.__pp
    
    @pp.setter
    def pp(self, pp):
        self.__pp = pp
    
    # remaining_pp
    @property
    def remaining_pp(self):
        return self.__remaining_pp
    
    @remaining_pp.setter
    def remaining_pp(self, remaining_pp):
        self.__remaining_pp = remaining_pp






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