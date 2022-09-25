from random import randint, random

from pokemon import Pokemon
from utility import rand_item, get_item


class Item:
    @classmethod
    def generate(cls):
        return rand_item([
            (PokeBall(), 9),
            (HealthPotion(), 8),
            (MovePotion(), 3)
            ])
    
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
    """A class extending the Item class which represents
    a Pokeball.
    """
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
    
    def use(self, pokemon, player):
        """Calculates whether a pokeball object catches a pokemon,
        and if so, adds it to pokemon collection.

        Args:
            pokemon (Pokemon): A pokemon object you are trying to catch.
            player (Player): The player object.

        Returns:
            bool: True or False indicating whether the pokemon was caught.
        """
        rand_num = random()
        health_remaining_factor = (
                (pokemon.hp-pokemon.remaining_hp)
                / pokemon.hp
                / 2)
        if rand_num <= self.catch_chance + (health_remaining_factor):
            player.pokemon.add(pokemon)
            print(f'Caught {pokemon.name}.')
            return True
        else:
            print(f'Failed to catch {pokemon.name}.')
            return False


class HealthPotion(Item):
    """A class extending the Item class which represents a Health Potion.
    """
    name = 'Health Potion'

    def __init__(self):
        super().__init__()
        self.__amount = 40
    
    def __repr__(self):
        return f'{self.name} (restores {self.__amount} hp for ' \
               'selected pokemon)'
    
    # amount
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    def use(self, pokemon):
        """Restores HP to a pokemon object

        Args:
            pokemon (Pokemon): A pokemon object in your collection.
        """
        pokemon.remaining_hp = ((pokemon.remaining_hp + self.amount)
                                if (pokemon.remaining_hp + self.amount)
                                <= pokemon.hp else pokemon.hp)



class MovePotion(Item):
    """A class extending the Item class which represents a
    Move Potion.
    """
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
        """Restores the PP of a chosen move.

        Args:
            pokemon (Pokemon): The pokemon object.
        """
        move = get_item(
                f"Use which move? {pokemon.available_moves_str}",
                pokemon.available_moves)
        move.remaining_pp = ((move.remaining_pp + self.amount)
                             if (move.remaining_pp + self.amount)
                             <= move.pp else move.pp)
