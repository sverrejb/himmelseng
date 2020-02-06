#!/usr/bin/env python3

"""this lambda reads all verse files from the verses-folder and bakes them into one for the app to use"""

import os
import json

PATH = 'verses/'
verses = []

for filename in os.listdir(PATH):
    with open(PATH + filename) as json_file:
        data = json.load(json_file)
        verses.append(data)

with open('src/verses.json', 'w', encoding='utf-8') as file:
    json.dump(verses, file, ensure_ascii=False)

print('{} verses built'.format(len(verses)))