#!/bin/bash

clear

echo "Checking and/or installing necessary files."

pip install -r requirements.txt

python3 main.py $1