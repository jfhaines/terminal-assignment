from item import Item, PokeBall, HealthPotion, MovePotion
from map import Map, Square
from moves import Move
from pokemon import Pokemon
from trainer import NpcTrainer, Player
from randomizer import RandomList
from utility import rand_unique_items, get_item, convert_list_to_prompt_str
from import_json import pokemon_data
from bag import ItemBag
import sys

mode = 'normal'
arg = sys.argv[1]
if arg == '--hard' or arg == '-h':
    mode = 'hard'
elif arg == '--easy' or arg == '-e':
    mode = 'easy'
elif arg == '--normal' or arg == '-n':
    pass

map = Map(10, 10)
player = Player()

if mode == 'easy':
    for i in range(3):
        player.pokemon.add(Pokemon.generate())
    for i in range(2):
        player.items.add(HealthPotion())
        player.items.add(PokeBall())
        player.items.add(MovePotion())
elif mode == 'hard':
        player.pokemon.add(Pokemon.generate())
else:
    for i in range(2):
        player.pokemon.add(Pokemon.generate())
    for i in range(1):
        player.items.add(HealthPotion())
        player.items.add(PokeBall())
        player.items.add(MovePotion())


map.set([0, 0], player)
me.move(map)
