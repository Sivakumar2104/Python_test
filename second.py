#! /usr/bin/python

import json
import sys
import os
import requests
print len(sys.argv)
if len(sys.argv) < 2:
    print "Usage : ./sdfsfdsdfsdf/py sdsfds"
    sys.exit(1)

with open('versions.json', 'r') as f:
    data = json.load(f)

print data["cap"]["PT"] 

data["cap"]["DEV"]=sys.argv[1]
with open('version.json', 'w') as f1:
    json.dump(data, f1, indent=4)

URL='https://code.bestbuy.com/'+data["cap"]["PT"]
print URL
r = requests.get(URL)
print r
