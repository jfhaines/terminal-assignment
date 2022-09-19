from random import randint, uniform

class Pokeball:
    catch_chance_range = [0.1, 0.5]

    @classmethod
    def __generate_random_catch_chance(cls):
        return round(uniform(cls.catch_chance_range[0], cls.catch_chance_range[1]) * 10) / 10

    @classmethod
    def generate(cls):
        return cls(cls.__generate_random_catch_chance())

    def __init__(self, catch_chance):
        self.catch_chance = catch_chance
        self.type = 'Pokeball'
    

class Potion:
    def __init__(self, uses, amount):
        self.uses = uses
        self.amount = amount


class MovePotion(Potion):
    uses_range = [1, 3]
    amount_range = [4, 15]
    
    @classmethod
    def __generate_random_uses(cls):
        return randint(cls.uses_range[0], cls.uses_range[1])

    @classmethod
    def __generate_random_amount(cls):
        return randint(cls.amount_range[0], cls.amount_range[1])

    @classmethod
    def generate(cls):
        return cls(cls.__generate_random_uses(), cls.__generate_random_amount())

    def __init__(self, uses, amount):
        super().__init__(uses, amount)
        self.type = 'Move Potion'


class HealthPotion(Potion):
    uses_range = [1, 3]
    amount_range = [60, 160]

    @classmethod
    def __generate_random_uses(cls):
        return randint(cls.uses_range[0], cls.uses_range[1])

    @classmethod
    def __generate_random_amount(cls):
        return randint(cls.amount_range[0], cls.amount_range[1])

    @classmethod
    def generate(cls):
        return cls(cls.__generate_random_uses(), cls.__generate_random_amount())

    def __init__(self, uses, amount):
        super().__init__(uses, amount)
        self.type = 'Health Potion'


def generate_item():
    rand_num = randint(1, 4)
    if rand_num == 1:
        return HealthPotion.generate()
    elif rand_num == 2:
        return MovePotion.generate()
    else:
        return Pokeball.generate()