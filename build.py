#!/usr/bin/env python3

import os
import json

PATH = 'verses/'

verses = []

for filename in os.listdir(PATH):
    with open(PATH + filename) as json_file:
        data = json.load(json_file)
        verses.append(data)

print(verses)

with open('src/verses.json', 'w') as file:
    json.dump(verses, file)

print(verses)