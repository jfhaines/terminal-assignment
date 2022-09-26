from random import randint

import names
import pause

from pokemon import Pokemon
from item import PokeBall, HealthPotion, MovePotion, Item
from custom_exceptions import InputError, NoneAvailableError, NoPokemonError
from utility import rand_item, should_continue
from bag import ItemBag, PokemonCollection


class Trainer:
    """A class that represents a Pokemon trainer.
    """    
    def __init__(self, name):
        self.__name = name
        self.__pokemon = PokemonCollection()
        self.__display_str = '!'
    
    def __repr__(self):
        return self.name

    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # pokemon
    @property
    def pokemon(self):
        return self.__pokemon
    
    @pokemon.setter
    def pokemon(self, pokemon):
        self.__pokemon = pokemon
    
    # display string
    @property
    def display_str(self):
        return self.__display_str
    
    @display_str.setter
    def display_str(self, display_str):
        self.__display_str = display_str



class NpcTrainer(Trainer):
    def __init__(self):
        super().__init__(names.get_first_name())
        for i in range(randint(1, 3)):
            self.pokemon.add(Pokemon.generate())



class Player(Trainer):
    def __init__(self):
        super().__init__(input('What is your name?: '))
        self.__items = ItemBag()
        self.__position = [0, 0]
        self.display_str = '@'
        self.pokemon.add(Pokemon.generate())
        self.items.add(PokeBall())
        self.items.add(HealthPotion())
    
    # items
    @property
    def items(self):
        return self.__items
    
    @items.setter
    def items(self, items):
        self.__items = items

    # position
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position
    

    def pokemon_battle(self, opponent_pokemon, is_catchable):
        """Allows a player to battle an opponent pokemon with
        their own pokemon.

        Args:
            opponent_pokemon (Pokemon): The opponent pokemon
            object.
            is_catchable (bool): Indicates whether the pokemon 
            can be caught or not.

        Returns:
            None or String: An 'exit' string value or None.
        """
        print(f'Your selected pokemon is {self.pokemon.active}. ' \
              f'You are facing {opponent_pokemon}.')
        while True:
            if self.pokemon.count_available == 0:
                raise NoPokemonError("You don't have any Pokemon available.")
            my_pokemon = self.pokemon.active
            option = input(
                    'What action to take? (0 = Use move, 1 = Use item, ' \
                    '2 = Switch Pokemon, 3 = Exit battle, ' \
                    '4 = Show items, 5 = Show Pokemon: ')
            try:
                if option == '0':
                    my_pokemon.use_move(opponent_pokemon)

                    if opponent_pokemon.remaining_hp == 0:
                        print(f'{my_pokemon.name_str} beat ' \
                              f'{opponent_pokemon.name_str}.')
                        return None
            
                    opponent_pokemon.use_move(my_pokemon, True)

                    if my_pokemon.remaining_hp == 0:
                        print(f'{opponent_pokemon.name_str} ' \
                              f'beat {my_pokemon.name_str}.')
                        continue

                elif option == '1':
                    if is_catchable:
                        caught = self.items.use(
                                my_pokemon, opponent_pokemon, self)
                        if caught == True:
                            return 'Exit'
                        else:
                            continue
                    else:
                        self.items.use(my_pokemon)
                        continue

                elif option == '2':
                    self.pokemon.switch()
                    continue

                elif option == '3':
                    return 'Exit'

                elif option == '4':
                    print(self.items)
                    continue

                elif option == '5':
                    print(self.pokemon)
                    continue

                else:
                    raise InputError(option)

            except InputError as err:
                print(err.user_message)
            except TypeError as err:
                print(err)
            except IndexError as err:
                print(err)
            except NoneAvailableError as err:
                print(err)


    def trainer_battle(self, trainer):
        """Allows a player object to battle against
        an NPC Trainer object.

        Args:
            trainer (NpcTrainer): An NpcTrainer object

        Returns:
            Str: A string value representing the outcome
            of the battle
        """
        if should_continue(
                f'Would you like to battle Pokemon Trainer '\
                f'{trainer.name}?') is False:
            return
        if (self.pokemon.count_available == 0 
            or trainer.pokemon.count_available == 0):
            raise NoPokemonError(
                    f"{'You do not' if self.pokemon.count_available == 0 else ('Pokemon Trainer ' + trainer.name + 'does not')} " \
                    f"have any available Pokemon. You can't battle.")
        while True:
            result = self.pokemon_battle(trainer.pokemon.active, False)
            if result == 'Exit':
                return 'Exit'

            if self.pokemon.count_available == 0:
                print(f'You have been defeated by {trainer.name}. ' \
                      f'You have no available Pokemon left.')
                return 'Lost'
            
            if trainer.pokemon.count_available == 0:
                print(f"You have won against {trainer.name}. " \
                      f"They have no Pokemon remaining.")
                return 'Won'

    def change_square(self, map, new_position):
        """Changes a player's position in the map's grid.

        Args:
            map (Map): The map object.
            new_position (List): A list representing coordinates.
        """
        map.set(new_position, self)
        map.set(self.position,
                (None 
                if not isinstance(map.get(self.position).former_val, Pokemon)
                else Pokemon.generate()))
        self.position = new_position


    def move(self, map):
        """Allows the player to move about the map and interact with it.

        Args:
            map (Map): The map object.
        """
        map.display()
        while True:
            try:
                action = input(
                        'What do you want to do? (a = Move Left, ' \
                        'd = Move Right, w = Move Up, s = Move Down, ' \
                        'i = Show Items, p = Show Pokemon, q = Quit: ')

                if action == 'i':
                    print(self.items)
                    map.display()
                    continue

                elif action == 'p':
                    print(self.pokemon)
                    map.display()
                    continue

                elif action == 'q':
                    break

                elif action == 'a':
                    new_position = [self.position[0], self.position[1] - 1]
                
                elif action == 'd':
                    new_position = [self.position[0], self.position[1] + 1]
                
                elif action == 'w':
                    new_position = [self.position[0] - 1, self.position[1]]

                elif action == 's':
                    new_position = [self.position[0] + 1, self.position[1]]

                else:
                    raise InputError(action)

            except InputError as err:
                print(err.user_message)
            except IndexError:
                print("Could not get new position.")
            
            else:
                try:
                    adj_square = map.get(new_position)

                    # Item
                    if isinstance(adj_square.current_val, Item):
                        self.items.pickup(
                                adj_square.current_val,
                                map, new_position)
                    
                    # Grass patch (pokemon)
                    elif isinstance(adj_square.current_val, Pokemon):
                        self.change_square(map, new_position)
                        map.display()
                        if rand_item([(True, 1), (False, 2)]) == True:
                            pause.milliseconds(800)
                            print(f'A wild {map.get(self.position).former_val} ' \
                                  f'appeared.')
                            self.pokemon_battle(
                                    map.get(self.position).former_val, True)
                        else:
                            continue
                    
                    # NPC Trainer
                    elif isinstance(adj_square.current_val, NpcTrainer):
                        if self.trainer_battle(adj_square.current_val) == 'Won':
                            map.set(new_position, None)
                    
                    elif adj_square.current_val == None:
                        self.change_square(map, new_position)
                
                except IndexError as err:
                    print(err)
                except TypeError as err:
                    print(err)
                except NoneAvailableError as err:
                    print(err)
                except NoPokemonError as err:
                    print(err)
                    print('Game Over')
                    break

            map.display()