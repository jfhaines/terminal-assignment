from item import Item, PokeBall, GreatBall, UltraBall, HealthPotion, SuperHealthPotion, MovePotion, SuperMovePotion
from map import Map, Square
from moves import Move
from pokemon import Pokemon
from trainer import NpcTrainer, Player


# map = Map(7, 7)
# me = Player.generate()
# map.set([0, 0], me)
# map.display()

p1 = Pokemon.generate()
p2 = Pokemon.generate()
t = Player.generate()

print(t.pokemon_battle(p1, p2))