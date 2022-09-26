#!/bin/bash

clear

echo "Checking and/or installing necessary files."

pip install -r requirements.txt

python3 set_pokemon_info_to_default.py