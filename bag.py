import pause

from pokemon import Pokemon
from item import PokeBall, HealthPotion, MovePotion
from custom_exceptions import NoneAvailableError, NoPokemonError
from utility import convert_list_to_prompt_str, get_item, should_continue


class ItemBag:
    """A class representing a player's item bag, provides
    interface for interacting with the various item type objects.
    """
    def __init__(self):
        self.__pokeballs = ItemType(PokeBall)
        self.__health_potions = ItemType(HealthPotion)
        self.__move_potions = ItemType(MovePotion)
    
    def __repr__(self):
        return f'{self.pokeballs.type.name}: ' \
               f'{self.pokeballs.count} remaining, ' \
               f'{self.health_potions.type.name}: ' \
               f'{self.health_potions.count} remaining, ' \
               f'{self.move_potions.type.name}: ' \
               f'{self.move_potions.count} remaining'

    @property
    def pokeballs(self):
        return self.__pokeballs
    
    @property
    def health_potions(self):
        return self.__health_potions
    
    @property
    def move_potions(self):
        return self.__move_potions
    
    def pickup(self, item, map_, item_position):
        """Adds an item to the item bag and removes the item
        from the map.

        Args:
            item (Item): A PokeBall, HealthPotion, or MovePotion instance
            map_ (Map): A map instance
            item_position (List): A list specifying coordinates
        """
        if should_continue(f'Do you want to pickup {item.name}?') is False:
            return
        self.add(item)
        map_.set(item_position, None)
        print(f'You picked up {item.name}. Item bag: {self}.')

    def add(self, item):
        """Looks at the item's class, and adds it to the correct item type
        object in item bag.

        Args:
            item (Item): A PokeBall, HealthPotion, or MovePotion instance
        """        
        if isinstance(item, PokeBall):
            self.pokeballs.add(item)
        
        elif isinstance(item, HealthPotion):
            self.health_potions.add(item)
        
        elif isinstance(item, MovePotion):
            self.move_potions.add(item)

        else:
            raise TypeError('Item being added is wrong type.')

    
    def available(self, is_catchable):
        """Gets a list of item type objects in item bag, which have more
        than one item in their collection.

        Args:
            is_catchable (bool): A bool value representing whether or not
            the pokemon is catchable.

        Returns:
            List: A list of item type objects.
        """
        available = []
        if not self.pokeballs.is_empty and is_catchable:
            available.append(self.pokeballs)

        if not self.health_potions.is_empty:
            available.append(self.health_potions)

        if not self.move_potions.is_empty:
            available.append(self.move_potions)
        return available
    
    def available_str(self, is_catchable):
        """Returns a string containing all available item types in item
        bag, and indicates which key to enter as input to select each
        item type.

        Args:
            is_catchable (bool): A bool value representing whether or
            not the pokemon is catchable.

        Raises:
            NoneAvailableError: An error class extending Exception,
            indicating that no items are available.
        Returns:
            Str: A string representation of the available item types.
        """
        if len(self.available(is_catchable)) > 0:
            return convert_list_to_prompt_str(self.available(is_catchable))
        else:
            raise NoneAvailableError('There are no item types available.')
    
    def use(self, my_pokemon, player, opponent_pokemon=None):
        """Asks user to select item, then uses it on a Pokemon.

        Args:
            my_pokemon (Pokemon): A pokemon object from player's collection
            opponent_pokemon (Pokemon, optional): An opponent pokemon
            object. Defaults to None.
            player (Player, optional): The player object. Defaults to None.

        Raises:
            TypeError: An error class indicating type incompatibility.

        Returns:
            bool: A bool value indicating whether or not a pokemon has
            been caught.
        """
        is_catchable = bool(opponent_pokemon)
        item_type = get_item(
                f"Which item to use? " \
                f"{self.available_str(is_catchable)}: ",
                self.available(is_catchable))
        if item_type.type == PokeBall:
            caught = item_type.get.use(opponent_pokemon, player)
        elif item_type.type == HealthPotion:
            item_type.get.use(player)
            caught = False
        elif item_type.type == MovePotion:
            item_type.get.use(my_pokemon)
            caught = False
        else: 
            raise TypeError(
                    'Could not use item, item type selected ' \
                    'is not supported.')
        item_type.remove()
        pause.milliseconds(800)
        print(f'Used {item_type.type.name}.')
        pause.milliseconds(800)
        return caught


class ItemType:
    """A class that provides an interface for storing and interacting
    with individual item objects of a specific type.
    """
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
        """Returns the count of objects in the collection.

        Returns:
            Int: Number of objects
        """
        return len(self.collection)
    
    def add(self, item):
        """Appends an item to the list stored in the collection
        attribute.

        Args:
            item (Item): A PokeBall, HealthPotion, or MovePotion
            instance.

        Raises:
            TypeError: An error class indicating type
            incompatibility.
        """
        if isinstance(item, self.type):
            self.collection.append(item)
        else:
            raise TypeError(
                    'Item being added to collection is the ' \
                    'incorrect type')
    
    @property
    def get(self):
        """Returns first object in the collection

        Raises:
            IndexError: Trying to access invalid index.

        Returns:
            Item: Either a PokeBall, HealthPotion, or
            MovePotion instance.
        """
        try:
            return self.collection[0]
        except IndexError:
            raise IndexError('Collection is empty, cannot retrieve item.')
    
    @property
    def is_empty(self):
        """Indicates if collection is empty

        Returns:
            bool: True or false value.
        """
        return True if self.count == 0 else False
    
    def remove(self):
        """Removes an item from the collection.

        Raises:
            IndexError: Trying to access invalid index.
        """        
        try:
            self.collection.pop()
        except IndexError:
            raise IndexError('Cannot remove item, collection is empty.')




class PokemonCollection():
    """A class that allows users to store pokemon objects and
    interact with them.
    """
    def __init__(self):
        self.__collection = []
    
    def __repr__(self):
        pokemon_list = []
        for pokemon in self.__collection:
            pokemon_list.append(str(pokemon))
        return f"{', '.join(pokemon_list)}"
    
    def add(self, pokemon):
        """Add pokemon to the pokemon collection.

        Args:
            pokemon (Pokemon): A pokemon object.

        Raises:
            TypeError: An error class indicating type
            incompatibility.
        """
        if isinstance(pokemon, Pokemon):
            self.__collection.append(pokemon)
        else:
            raise TypeError('Object being added is not a Pokemon.')
    
    @property
    def available(self):
        """Returns a list of pokemon with available hp.

        Returns:
            List: List of pokemon objects.
        """
        available = []
        for pokemon in self.__collection:
            if pokemon.remaining_hp > 0:
                available.append(pokemon)
        return available
    
    @property
    def available_str(self):
        """Returns a string which lists available pokemon,
        and which key the user should enter to select each pokemon.

        Returns:
            String: String of pokemon.
        """
        if len(self.available) > 0:
            return convert_list_to_prompt_str(self.available)
        else:
            raise NoPokemonError('Trainer has no pokemon with remaining HP.')
        

    @property
    def all(self):
        return self.__collection
    
    @property
    def all_str(self):
        """Returns a string which lists all pokemon,
        and which key the user should enter to select each pokemon.

        Returns:
            String: String of pokemon.
        """
        if len(self.all) > 0:
            return convert_list_to_prompt_str(self.all)
        else:
            raise NoPokemonError('Trainer has no pokemon.')
    
    @property
    def active(self):
        """Returns the first pokemon in the available list.

        Raises:
            NoPokemonError: No pokemon are available.

        Returns:
            Pokemon: A pokemon object
        """
        try:
            pokemon = self.available[0]
            return pokemon
        except IndexError:
            raise NoPokemonError('No pokemon are available.')
    
    @property
    def count_available(self):
        """Counts all pokemon with remaining hp.

        Returns:
            Int: Number of remaining pokemon with hp left.
        """
        return len(self.available)

    def switch(self):
        """Asks the user to select a pokemon, and changes the
        active pokemon to that pokemon.
        """
        if len(self.available) <= 1:
            raise NoneAvailableError(
                    "You don't have another " \
                    "Pokemon to switch to.")

        pokemon = get_item(
                f"Which Pokemon do you want to use? " \
                f"{self.available_str}: ", self.available)
        self.__collection.remove(pokemon)
        self.__collection.insert(0, pokemon)
        pause.milliseconds(800)
        print(f"Switched to {self.active.name}.")
        pause.milliseconds(800)