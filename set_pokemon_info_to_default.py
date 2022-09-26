import json

# Reset the pokemon-info.json file to contain
# the information in pokemon-info-backup.json
# (used in the case of data corruption or if the PokeBase
# module breaks)

with open('pokemon-info-backup.json', 'r') as f:
    info = f.read()
    pokemon_data = json.loads(info)

json_pokemon = json.dumps(pokemon_data)
with open('pokemon-info.json', 'w') as f:
    f.write(json_pokemon)