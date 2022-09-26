#!/bin/bash

clear

echo "Checking and/or installing necessary files."

pip install -r requirements.txt

python3 store_json_pokemon.py $1