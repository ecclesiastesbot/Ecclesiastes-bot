#!/usr/bin/env python3
import json

def get_verselist():
    filename = "ecclesiastes.json"
    f = open(filename, 'r')
    data = json.load(f)
    verselist = []
    for chapter in range(0, 12):
        verses = data["chapters"][chapter]["verses"]
        for i in range(0, len(verses)):
            for v in verses[i].values():
                verselist.append(v)
    
    return verselist
