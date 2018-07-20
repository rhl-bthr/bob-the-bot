import os
import re
import pytz
import json
import random
import datetime
# import all data from const.py
from const import *

""" maps some similar user words onto known words """
with open("db/mapping.json") as map_file:
    mapping = json.load(map_file)


def getFile(paths, types="file"):
    """get files for messages formatted according to API (json). """
    if not isinstance(paths, list):
        paths = [paths]
    data = []
    for path in paths:
        data.append({
            "message": {
                "attachment": {
                    "type": types,
                    "payload": {
                        "url": path,
                        "is_reusable": True
                    }
                }
            }
        })
    return data

# get relevant phone numbers / contacts / links / lists
# entities is a list
# subjects is a list
# append_text: text to be appended to a message according to types


def getNum(entities, subjects, types=None, append_text=None):
    """
    Get phone numbers / contacts / links for messages formaatted according to API (json).

    Arguements:
    entities -
    subjects - titles for data (for buttons)
    types - type of data (phone number/contact/link/list)
    append_text - text to be appended to specify type of data given by BOB.

    Returns:
    formatted message with required fields.
    """
    data, buttons = [], []
    payload_type = "payload"
    if types == "postback" and not append_text:
        append_text = "Here's the list to choose from:"
    elif types == "phone_number":
        append_text = "Here's the contact:"
    elif types == "web_url":
        append_text = "Here's the link:"
        payload_type = "url"

    if not isinstance(entities, list):
        entities, subjects = [entities], [subjects]
    for x in range(len(entities)):
        buttons.append({
            "type": types,
            "title": subjects[x],
            payload_type: entities[x]
        })

    # buttons are grouped in 3s and stored in lists
    #[ [b1,b2,b3], [b4,b5,b6] [b7,b8,b9], ... ]
    buttons = [buttons[x:x + 3] for x in range(0, len(buttons), 3)]
    for x in range(len(buttons)):
        data.append({
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "button",
                        "text": append_text,
                        "buttons": buttons[x]
                    }
                }
            }
        })
    return data


def getText(texts, entity=None):
    """
    Get text formatted according to API (json).

    Arguements:
    texts - list of texts or a single text
    entity - info to be added before the text

    Returns:
    A dictionary formatted as:
    [ {"message","text"}, {"message","text"}, ... ]
    """
    if not isinstance(texts, list):
        texts = [texts]
    texts, data = list(texts), []
    if entity:
        texts = [entity + ":\n" + text for text in texts]
    for text in texts:
        text = re.sub(' +', ' ', text)
        data.append({
            "message": {
                "text": text,
            }
        })
    return data


def sayHello(name):
    """ Hello message with randomized words along with name. """
    INTRO_PREF = ["Hey,", "Hi,", "Whassup", "Yo"]
    INTRO_MSG = ["I'm BOB!", "It's me, BOB!", "My name is BOB!"]
    INTRO_MSG_CONTENT = createRandomText(INTRO_PREF, name + "\n", INTRO_MSG)

    return getText(
        [random.choice(INTRO_MSG_CONTENT) + " :D", "Type 'help' to see the query guide."])


def saySorry(name):
    """ sorry message with randomized words. """
    SRY_PREF = ["Hey", "Hi", "Sorry", "Umm,", "Err", "Whoops"]
    SRY_MSG = ["Dunno what you asked for :(", "I Didn't get you.",
               "I ain't that smart", "I have failed you :("]
    HELP_MSG = ["Typing help might help", "Need help? type help"]

    SRY_MSG_CONTENT = createRandomText(SRY_PREF, name + "\n", SRY_MSG)
    return getText([
        random.choice(SRY_MSG_CONTENT), random.choice(HELP_MSG) + " :)"])


def createRandomText(prefix, name, content):
    MSG = [x + " " + name + y
           for x in prefix for y in content]
    return MSG


def getMeal(mealtype):
    """ Get today's meal. mealtype: breakfast / lunch / dinner. """
    now = datetime.datetime.now(
        pytz.timezone(
            'Asia/Kolkata')).date(
    ).strftime(
                '%d-%m-%Y')
    todays_menu_file = os.path.join('db', 'menu', now + ".json")
    try:
        with open(todays_menu_file) as json_data:
            today = json.load(json_data)
        return "\n".join(today[mealtype])
    except:
        return "<Sorry, Menu will be updated by tonight>"
