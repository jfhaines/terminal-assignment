class Pokeball:
    def __init__(self, catch_chance):
        self.catch_chance = catch_chance
    
class Potion:
    def __init__(self, uses, amount):
        self.uses = uses
        self.amount = amount

class Move_Potion(potion):
    pass

class Health_Potion(potion):
    pass