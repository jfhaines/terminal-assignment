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
        return f'{self.name} (power: {self.power}, pp: {self.remaining_pp}/{self.pp})'

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


