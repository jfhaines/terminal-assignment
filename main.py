from item import Item, PokeBall, HealthPotion, MovePotion
from map import Map, Square
from moves import Move
from pokemon import Pokemon
from trainer import NpcTrainer, Player
from randomizer import RandomList
from utility import rand_unique_items, get_item, convert_list_to_prompt_str
from import_json import pokemon_data
from bag import ItemBag

i = ItemBag()
m = Map(5, 5)
p = [1, 1]

print(convert_list_to_prompt_str([]))


# map = Map(7, 7)
# me = Player()
# map.set([0, 0], me)

# me.move(map)




# p1 = Pokemon.generate()
# p2 = Pokemon.generate()
# p3 = Pokemon.generate()
# ball = PokeBall()
# health_potion = HealthPotion()
# move_potion = MovePotion()
# t = Player.generate()
# t.items.pickup(ball)
# t.items.pickup(health_potion)
# t.items.pickup(move_potion)
# t.pokemon.add(p1)
# t.pokemon.add(p2)
# t.pokemon_battle(p1, p3)

# p = PokeBall()
# h = HealthPotion()
# t.items.pickup(p)
# t.items.pickup(h)
# print(t.items.available_str)
