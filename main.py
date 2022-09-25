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
print(me.items)
map.set([0, 0], me)
me.move(map)





# player = Player()
# player.pokemon.add(Pokemon.generate())
# opponent_pokemon = Pokemon.generate()

# before_active = player.pokemon.active
# before_collection = player.pokemon.all
# before_available = player.pokemon.available


# player.pokemon_battle(opponent_pokemon, True)

# after_active = player.pokemon.active
# after_collection = player.pokemon.all
# after_available = player.pokemon.available


# print('here')

# print('before_active: ' + before_active + 'before_collection: ' + before_collection + 'before_active: ' + before_active)
# print('---------')
# print('after_active: ' + after_active + 'after_collection: ' + after_collection + 'after_active: ' + after_active)