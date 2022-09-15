class move:
    def __init__(self, name, damage, max_number_of_moves):
        self.name = name
        self.damage = damage
        self.max_number_of_moves = max_number_of_moves
        self.remaining_number_of_moves = max_number_of_moves