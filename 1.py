#! /usr/bin/python

import json
import sys
import os

with open('versions.json', 'r') as file:
    data = json.load(file)


print data["cap"]["PT"]

data["cap"]["coreblue"]="3.0"

with open('versions.json', 'w') as file1:
    json.dump(data, file1, indent=4)

