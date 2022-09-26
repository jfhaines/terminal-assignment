import pokebase as pb
import pause

from random import randint

from import_json import pokemon_data, move_data
from moves import Move
from custom_exceptions import NoneAvailableError
from utility import rand_unique_items, convert_list_to_prompt_str, get_item


class Pokemon:
    """A class representing a Pokemon
    """

    @classmethod
    def generate(cls):
        """A function used for randomly generating a Pokemon object.

        Returns:
            Pokemon: A pokemon object.
        """
        while True:
            try:
                pokemon_name = rand_unique_items(1, list(pokemon_data.keys()))
                stats = pokemon_data[pokemon_name]

            except KeyError:
                print('Unable to load Pokemon.')
                return None

            try:
                available_moves = []
                for move in pokemon_data[pokemon_name]['moves']:
                    if move in move_data:
                        available_moves.append(move)
                if available_moves < 2:
                    continue

                moves = rand_unique_items(4, available_moves)
                for index, move_name in list(enumerate((moves))):
                    move_stats = move_data[move_name]
                    moves[index] = Move(move_name, move_stats['power'],
                                        move_stats['pp'])
                break
            
            except KeyError:
                print('Unable to load move data.')
                break

        return cls(name = pokemon_name, hp = stats['hp'],
                   attack = stats['attack'], defense = stats['defense'],
                   moves = moves)
    
    def __repr__(self):
        return f"{self.name_str} (HP: {self.remaining_hp}/{self.hp}, " \
               f"Attack: {self.attack}, Defense: {self.defense})"

    def __init__(self, name, hp, attack, defense, moves):
        self.__name = name
        self.__hp = hp
        self.__remaining_hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__moves = moves
        self.__display_str = '*'

    # name
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    # hp
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, hp):
        self.__hp = hp
    
    # remaining_hp
    @property
    def remaining_hp(self):
        return self.__remaining_hp
    
    @remaining_hp.setter
    def remaining_hp(self, remaining_hp):
        self.__remaining_hp = remaining_hp
    
    # attack
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self, attack):
        self.__attack = attack
    
    # defense
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self, defense):
        self.__defense = defense
    
    # moves
    @property
    def moves(self):
        return self.__moves
    
    @moves.setter
    def moves(self, moves):
        self.__moves = moves

    # display string
    @property
    def display_str(self):
        return self.__display_str
    
    @display_str.setter
    def display_str(self, display_str):
        self.__display_str = display_str
    
    def use_move(self, opponent_pokemon, attacking_pokemon_is_npc=False):
        """Picks a Pokemon move, and uses that move on another pokemon,
        dealing it damage.

        Args:
            opponent_pokemon (Pokemon): A Pokemon object being attacked
            attacking_pokemon_is_npc (bool, optional): Indicates whether
            or not an NPC is attacking. Defaults to False.
        """
        if self.available_moves == 0:
            raise NoneAvailableError(
                    f"{self.name_str} has no moves available.")
        if attacking_pokemon_is_npc:
            move = rand_unique_items(1, self.available_moves)
        else:
            move = get_item(
                    f"Use which move? {self.available_moves_str}: ",
                    self.available_moves)
        damage = int((((((((2 * 20/5 + 2)
                 * self.attack
                 * move.power)
                 / opponent_pokemon.defense) / 50) + 2)
                 * randint(217, 255)) / 255))
        opponent_pokemon.remaining_hp = (
                0 if damage
                > opponent_pokemon.remaining_hp
                else opponent_pokemon.remaining_hp
                - damage)
        move.remaining_pp -= 1
        pause.milliseconds(800)
        print (f'{self.name_str} used {move.name} dealing {damage} damage. ' \
               f'{opponent_pokemon.name_str} has ' \
               f'{opponent_pokemon.remaining_hp}/{opponent_pokemon.hp} ' \
               f'hp remaining.')
        pause.milliseconds(800)


    @property
    def available_moves(self):
        """Returns a list of moves with PP remaining.

        Returns:
            List: A list of move objects
        """
        available = []
        for move in self.moves:
            if move.remaining_pp > 0:
                available.append(move)
        return available
    
    @property
    def available_moves_str(self):
        """Returns a string of available moves, and shows the user what
        key to press to select each move. 

        Returns:
            String: A string consisting of available moves.
        """
        if len(self.available_moves) > 0:
            return convert_list_to_prompt_str(self.available_moves)
        else:
            raise NoneAvailableError(
                f"{self.name_str} has no moves available.")
    
    @property
    def all_moves_str(self):
        """Returns a string of all moves, and shows the user what key
        to press to
        select each move.

        Returns:
            String: A string consisting of all moves.
        """
        if len(self.moves) > 0:
            return convert_list_to_prompt_str(self.moves)
        else:
            raise NoneAvailableError(f"{self.name_str} has no moves.")

    @property
    def name_str(self):
        return ' '.join(self.name.split('-')).capitalize()