from random import randint, random
from pokemon import Pokemon

class Item:
    @classmethod
    def generate(cls):
        rand_num = randint(1, 20)
        if rand_num <= 10:
            return PokeBall()
        elif rand_num <= 15:
            return HealthPotion()
        else:
            return MovePotion()
    
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
    name = "Poke Ball"

    def __init__(self):
        super().__init__()
        self.__catch_chance = 0.3
    
    def __repr__(self):
        return f'{self.name} (used to catch Pokemon)'
    
    # catch chance
    @property
    def catch_chance(self):
        return self.__catch_chance
    
    @catch_chance.setter
    def catch_chance(self, catch_chance):
        self.__catch_chance = catch_chance
    
    def use(self, pokemon, player, map, item_position):
        rand_num = random()
        health_remaining_factor = (pokemon.hp - pokemon.remaining_hp) / pokemon.hp / 2
        if rand_num <= self.catch_chance + (health_remaining_factor):
            player.pokemon.add(pokemon)
            map.set(item_position, None)
            print(f'Caught {pokemon.name}.')
            return
        else:
            print(f'Failed to catch {pokemon.name}.')
            return


class HealthPotion(Item):
    name = 'Health Potion'

    def __init__(self):
        super().__init__()
        self.__amount = 40
    
    def __repr__(self):
        return f'{self.name} (restores {self.__amount} hp for selected pokemon)'
    
    # amount
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    def use(self, pokemon):
        pokemon.remaining_hp = pokemon.remaining_hp + self.amount if (pokemon.remaining_hp + self.amount) <= pokemon.hp else pokemon.hp



class MovePotion(Item):
    name = 'Move Potion'

    def __init__(self):
        super().__init__()
        self.__amount = 10
    
    def __repr__(self):
        return f'{self.name} (restores {self.__amount} pp for selected move)'
    
    # amount
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    
    def use(self, pokemon):
        move_index = int(input(f"Use which move? {pokemon.available_moves_str}"))
        move = pokemon.available_moves[move_index]
        move.remaining_pp = (move.remaining_pp + self.amount) if (move.remaining_pp + self.amount) <= move.pp else move.pp
