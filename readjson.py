#! /usr/bin/python

import json

with open('sample.json', 'r') as f:
    data = json.load(f)
    data["address"]["state"]='AR'
    print data

with open('sample.json', 'w') as f1:
    json.dump(data, f1, indent=4)


"""print data["phoneNumbers"]

for x in data["phoneNumbers"]:
    print x["type"]

print data["address"]["streetAddress"]

for y in data["address"]:
    print data["address"][y]"""
