""" Load actual BOB data from db/database.json. to 'db'. """

# from database import *
import json

with open("db/database.json") as f:
    db = json.load(f)
