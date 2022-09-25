from random import randint

from pokemon import Pokemon
from item import Item
from trainer import NpcTrainer, Player
from utility import rand_item


class Square:
    """A class which represents a square on the map, which
    has a current value and former value. 
    """
    @classmethod
    def generate(cls):
        """Generates a square object, with its current
        value set to a random item/pokemon/trainer.

        Returns:
            Square: Returns a square object.
        """        
        return cls(rand_item([
            (None, 15), (Pokemon.generate(), 6),
            (Item.generate(), 8), (NpcTrainer(), 2)
            ]), None)

    def __init__(self, current_val, former_val):
        self.__current_val = current_val
        self.__former_val = former_val
    
    def __str__(self):
        if self.__current_val == None:
            return ' '
        else:
            return self.__current_val.display_str
    
    #current_val
    @property
    def current_val(self):
        return self.__current_val
    
    @current_val.setter
    def current_val(self, current_val):
        self.__current_val = current_val
    
    #former_val
    @property
    def former_val(self):
        return self.__former_val
    
    @former_val.setter
    def former_val(self, former_val):
        self.__former_val = former_val



class Map:
    """A class which represents the map a player moves around on.
    """    
    def __init__(self, rows, columns):
        self.grid = []
        for i in range(rows):
            self.grid.append([])
        for row in self.grid:
            for column_num in range(columns):
                row.append(Square.generate())
    
    def get(self, coordinates):
        """Retrieves the square object at the given coordinates on
        the map.

        Args:
            coordinates (List): A list representing coordinates.

        Raises:
            IndexError: Trying to access an invalid index.

        Returns:
            Square: A square object.
        """
        try:
            row_num, col_num = coordinates
            return self.grid[row_num][col_num]
        except IndexError:
            raise IndexError('Coordinates not valid.')
    
    def set(self, coordinates, value):
        """Sets the current value of a square object at the given
        coordinates on the map.

        Args:
            coordinates (List): A list representing coordinates.
            value (Item/Trainer/Pokemon): Either an Item, Trainer
            or Pokemon object.

        Raises:
            IndexError: _description_
        """
        try:
            row_num, col_num = coordinates
            square = self.grid[row_num][col_num]
        except IndexError:
            raise IndexError('Coordinates are not valid.')
        square.former_val = self.grid[row_num][col_num].current_val
        square.current_val = value
        

    def display(self):
        """Prints the map to the screen.
        """
        try:
            for col in self.grid[0]:
                print('----', end='')
            print('---\n')
            for row in self.grid:
                for square in row:
                    print(square, end='    ')
                print('\n')
            for col in self.grid[0]:
                print('----', end='')
            print('---\n')
        except IndexError:
            print('Map is empty.')
    
    def clear_square(self, coordinates):
        self.set(coordinates, None)

