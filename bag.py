from pokemon import Pokemon
import pokebase as pb
from item import PokeBall, HealthPotion, MovePotion, Item
from custom_exceptions import InputError
from utility import get_index


class ItemBag:
    def __init__(self):
        self.__pokeballs = ItemType(PokeBall)
        self.__health_potions = ItemType(HealthPotion)
        self.__move_potions = ItemType(MovePotion)
    
    def __repr__(self):
        return f'{self.pokeballs.type.name}: {self.pokeballs.count} remaining, {self.health_potions.type.name}: {self.health_potions.count} remaining, {self.move_potions.type.name}: {self.move_potions.count} remaining'

    @property
    def pokeballs(self):
        return self.__pokeballs
    
    @property
    def health_potions(self):
        return self.__health_potions
    
    @property
    def move_potions(self):
        return self.__move_potions
    
    def pickup(self, item):
        if isinstance(item, PokeBall):
            self.pokeballs.add(item)
        
        elif isinstance(item, HealthPotion):
            self.health_potions.add(item)
        
        elif isinstance(item, MovePotion):
            self.move_potions.add(item)
    
    def available(self, is_catchable):
        available = []
        if not self.pokeballs.is_empty and is_catchable:
            available.append(self.pokeballs)

        if not self.health_potions.is_empty:
            available.append(self.health_potions)

        if not self.move_potions.is_empty:
            available.append(self.move_potions)
        return available
    
    def available_str(self, is_catchable):
        list_store = list(enumerate(self.available(is_catchable)))
        for index, item in list_store:
            list_store[index] = f'{index} = {item}'
        return ', '.join(list_store)
    
    def use(self, my_pokemon, opponent_pokemon=None):
        is_catchable = bool(opponent_pokemon)
        while True:
            if len(self.available(is_catchable)) == 0:
                print('No available items')
                return
            try:
                item_index = get_index(f"Which item to use? {self.available_str(is_catchable)}: ", self.available(is_catchable))
            except InputError as err:
                print(err.user_message)
            else:
                item_type = self.available(is_catchable)[item_index]
                if item_type.type == PokeBall:
                    caught = item_type.get.use(opponent_pokemon, self)
                else:
                    item_type.get.use(my_pokemon)
                    caught = False
                item_type.remove()
                print(f'Used {item_type.type.name}.')
                return caught


class ItemType:
    def __init__(self, type):
        self.__collection = []
        self.__type = type
    
    def __repr__(self):
        return f"{self.type()} ({self.count} remaining)"
    
    @property
    def collection(self):
        return self.__collection

    @property
    def type(self):
        return self.__type

    @property
    def count(self):
        return len(self.collection)
    
    def add(self, item):
        if isinstance(item, self.type):
            self.collection.append(item)
    
    @property
    def get(self):
        return self.collection[0] if not self.is_empty else None
    
    @property
    def is_empty(self):
        return True if self.count == 0 else False
    
    def remove(self):
        self.collection.pop()




class PokemonCollection():
    def __init__(self):
        self.__collection = []
    
    def __repr__(self):
        pokemon_list = []
        for pokemon in self.__collection:
            pokemon_list.append(str(pokemon))
        return f"{', '.join(pokemon_list)}"
    
    def add(self, pokemon):
        self.__collection.append(pokemon)
    
    @property
    def available(self):
        available = []
        for pokemon in self.__collection:
            if pokemon.remaining_hp > 0:
                available.append(pokemon)
        return available
    
    @property
    def available_str(self):
        list_store = list(enumerate(self.available))
        for index, pokemon in list_store:
            list_store[index] = f"{index} = {pokemon}"
        return ', '.join(list_store)

    @property
    def all(self):
        return self.__collection

    def switch(self, index):
        pokemon = self.available[index]
        self.__collection.remove(pokemon)
        self.__collection.insert(0, pokemon)
    
    @property
    def active(self):
        return self.available[0]
    
    @property
    def count_available(self):
        return len(self.available)