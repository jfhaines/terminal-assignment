from random import randint, random
from pokemon import Pokemon

class Item:
    @classmethod
    def generate(cls):
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
    
    def __init__(self):
        self.__display_str = '?'
    
    # display string
    @property
    def display_str(self):
        return self.__display_str
    
    @display_str.setter
    def display_str(self, display_str):
        self.__display_str = display_str




class PokeBall(Item):
    def __init__(self):
        super().__init__()
        self.__catch_chance = 0.2
        self.__type = 'Poke Ball'
        self.__name = 'Poke Ball'
    
    # catch chance
    @property
    def catch_chance(self):
        return self.__catch_chance
    
    @catch_chance.setter
    def catch_chance(self, catch_chance):
        self.__catch_chance = catch_chance
    
    # type
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
    
    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    

    def use(self, pokemon):
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





class HealthPotion(Item):
    def __init__(self):
        super().__init__()
        self.__amount = 30
        self.__type = 'Health Potion'
        self.__name = 'Health Potion'
    
    # amount
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

     # type
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
    
    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name


    def use(self, pokemon):
        pokemon.remaining_hp = pokemon.remaining_hp + self.amount if (pokemon.remaining_hp + self.amount) <= pokemon.hp else pokemon.hp

class SuperHealthPotion(HealthPotion):
    def __init__(self):
        super().__init__()
        self.amount = 60
        self.name = 'Super Health Potion'



class MovePotion(Item):
    def __init__(self):
        super().__init__()
        self.__amount = 8
        self.__type = 'Move Potion'
        self.__name = 'Move Potion'
    
    # amount
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

     # type
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
    
    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    def use(self, move):
        move.remaining_pp = move.remaining_pp + self.amount if (move.remaining_pp + self.amount) <= move.pp else move.pp


class SuperMovePotion(MovePotion):
    def __init__(self):
        super().__init__()
        self.amount = 20
        self.name = 'Super Move Potion'



