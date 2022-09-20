from random import randint, random
from pokemon import Pokemon

class PokeBall:
    def __init__(self):
        self.catch_chance = 0.2
        self.type = 'Poke Ball'
        self.name = 'Poke Ball'
    
    def catch(self, pokemon):
        rand_num = random()
        health_remaining_factor = (pokemon.hp - pokemon.remaining_hp) / pokemon.hp / 2
        if rand_num > self.catch_chance + (health_remaining_factor):
            return False
        else:
            return True

class GreatBall(PokeBall):
    def __init__(self):
        super().__init__()
        self.catch_chance = 0.4
        self.name = 'Great Ball'

class UltraBall(PokeBall):
    def __init__(self):
        super().__init__()
        self.catch_chance = 0.6
        self.name = 'Ultra Ball'




class HealthPotion:
    def __init__(self):
        self.amount = 30
        self.type = 'Health Potion'
        self.name = 'Health Potion'

class SuperHealthPotion(HealthPotion):
    def __init__(self):
        super().__init__()
        self.amount = 60
        self.name = 'Super Health Potion'



class MovePotion:
    def __init__(self):
        self.amount = 8
        self.type = 'Move Potion'
        self.name = 'Move Potion'

class SuperMovePotion(MovePotion):
    def __init__(self):
        super().__init__()
        self.amount = 20
        self.name = 'Super Move Potion'



def generate_item():
    rand_num = randint(1, 20)
    if rand_num <= 4:
        return PokeBall()
    elif rand_num <= 6:
        return GreatBall()
    elif rand_num <= 8:
        return UltraBall()
    elif rand_num <= 12:
        return HealthPotion()
    elif rand_num <= 14:
        return SuperHealthPotion()
    elif rand_num <= 18:
        return MovePotion()
    else:
        return SuperMovePotion()


p1 = Pokemon.generate()
p2 = Pokemon.generate()
move = p1.moves[list(p1.moves.keys())[0]]

p1.use_move(move, p2)