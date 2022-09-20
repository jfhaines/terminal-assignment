from random import randint

class Map:
    def __init__(self, rows, columns):
        self.grid = []
        for i in range(rows):
            self.grid.append([])
        for row in self.grid:
            for column_num in range(columns):
                num = randint(1, 30)
                if num <= 15:
                    row.append(' ')
                elif num <= 24:
                    row.append('*')
                elif num <= 28:
                    row.append('?')
                elif num <= 30:
                    row.append('!')

    def display(self):
        for row in self.grid:
            for square in row:
                print(square, end='    ')
            print('\n')

pokemon_map = Map(7, 7)