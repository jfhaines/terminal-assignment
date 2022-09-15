class pokemon:
    def __init__(self, name, total_health, move_list):
        self.name = name
        self.total_health = total_health
        self.current_health = total_health
        self.moves = moves