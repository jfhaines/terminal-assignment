import json


with open('pokemon-info.json', 'r') as f:
    info = f.read()
    pokemon_data = json.loads(info)

with open('moves-info.json', 'r') as f:
    info = f.read()
    move_data = json.loads(info)
