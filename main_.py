from item import Item, PokeBall, HealthPotion, MovePotion
from map import Map, Square
from moves import Move
from pokemon import Pokemon
from trainer import NpcTrainer, Player
from randomizer import RandomList
from utility import rand_unique_items, get_item, convert_list_to_prompt_str
from import_json import pokemon_data
from bag import ItemBag


map = Map(7, 7)
me = Player()
map.set([0, 0], me)
me.move(map)
