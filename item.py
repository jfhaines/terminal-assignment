class pokeball:
    def __init__(self, catch_chance):
        self.catch_chance = catch_chance
    
class potion:
    def __init__(self, uses, amount):
        self.uses = uses
        self.amount = amount

class move_potion(potion):
    pass

class health_potion(potion):
    pass