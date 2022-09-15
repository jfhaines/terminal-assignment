class map:
    def __init__(self, rows, columns):
        self.grid = []
        for row in range(rows):
            self.grid.append([])
        for row in self.grid:
            for column in range(columns):
                row.append('*')

    def display(self):
        for row in self.grid:
            for square in row:
                print(square, end='   ')
            print('\n')

pokemon_map = map(4, 4)
pokemon_map.display()