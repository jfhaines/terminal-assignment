from item import PokeBall, HealthPotion, MovePotion
from map import Map
from moves import Move
from pokemon import Pokemon
from trainer import Player
import sys
import pause


mode = 'normal'
arg = sys.argv[1]
if arg == '--hard' or arg == '-h':
    mode = 'hard'
elif arg == '--easy' or arg == '-e':
    mode = 'easy'
elif arg == '--normal' or arg == '-n':
    pass

print("\n"
      "\n"
      "Welcome to the Kanto region. This world is full of pokemon. " \
      "Here, you can move around the map, collect items, " \
      "catch pokemon and battle trainers. The '@' symbol on the map " \
      "represents your player. The '?' symbol represents an item. " \
      "The '!' symbol represents a trainer. The '*' symbol " \
      "represents a patch of grass (which sometimes contain pokemon)." \
      "Each Pokemon has HP representing their health, use a health potion "
      "if it gets low. Each Pokemon has a set of moves. Each move " \
      "has different damage. Each time you use a move, the move's PP will "
      "decrease by 1. If it drops to 0, use a Move Potion to restore PP, " \
      "so that you can keep using that move. Use a PokeBall on wild Pokemon " \
      "to try and catch them. The lower the opponent Pokemon's HP, the more " \
      "likely you are to catch them. Once caught, the Pokemon will be " \
      "added to your collection, and you can switch to it in battle. "
      "If you have no pokemon with HP remaining, the game ends. Good luck! \n")

map = Map(10, 10)

pause.seconds(0.5)

player = Player()

if mode == 'easy':
    for i in range(2):
        player.pokemon.add(Pokemon.generate())
    for i in range(2):
        player.items.add(HealthPotion())
        player.items.add(PokeBall())
        player.items.add(MovePotion())
elif mode == 'hard':
    pass
else:
    player.pokemon.add(Pokemon.generate())
    for i in range(1):
        player.items.add(HealthPotion())
        player.items.add(PokeBall())
        player.items.add(MovePotion())

map.set([0, 0], player)

player.move(map)
