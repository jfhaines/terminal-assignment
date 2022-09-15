from contextlib import AsyncExitStack


class Move:
    def __init__(self, name, type, damage, max_number_of_moves):
        self.name = name
        self.type = type
        self.damage = damage
        self.max_number_of_moves = max_number_of_moves
        self.remaining_number_of_moves = max_number_of_moves

move_list = [
    Move('Thunderbolt', 'Electric', 20, 3),
    Move('Volt Tackle', 'Electric', 11, 15),
    Move('Shock Wave', 'Electric', 15, 6),
    Move('Flamethrower', 'Fire', 22, 4),
    Move('Fire Blast', 'Fire', 15, 7),
    Move('Flame Burst', 'Fire', 12, 12),
    Move('Hydro Pump', 'Water', 22, 4),
    Move('Water Pulse', 'Water', 15, 7),
    Move('Water Gun', 'Water', 12, 12),
    Move('Waterfall', 'Water', 19, 6),
    Move('Leaf Blade', 'Grass', 12, 12),
    Move('Giga Drain', 'Grass', 15, 7),
    Move('Leaf Storm', 'Grass', 22, 4),
    Move('Confusion', 'Psychic', 15, 7),
    Move('Cosmic Power', 'Psychic', 24, 3),
    Move('Psybeam', 'Psychic', 15, 6),
    Move('Hyperbeam', 'Standard', 25, 3),
    Move('Quick Attack', 'Standard', 13, 9),
    Move('Tackle', 'Standard', 10, 17),
    Move('Take Down', 'Standard', 11, 10),
    Move('Crunch', 'Standard', 15, 9)
]