from random import randint

class Map:
    def __init__(self, rows, columns):
        self.grid = []
        for row in range(rows):
            self.grid.append([])
        for row in self.grid:
            for column in range(columns):
                row.append(' ')

    def display(self):
        for row in self.grid:
            for square in row:
                print(square, end='    ')
            print('\n')

    def randomise(self):
        for row in self.grid:
            for i, v in enumerate(row):
                num = randint(1, 30)
                if num <= 15:
                    pass
                elif num <= 24:
                    row[i] = '*'
                elif num <= 28:
                    row[i] = '?'
                elif num <= 30:
                    row[i] = '!'

pokemon_map = Map(7, 7)
pokemon_map.randomise()
pokemon_map.display()