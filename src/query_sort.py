""" Manipulate user queries. """

import requests
import re
import os
import pytz
import json
import random
import datetime
from api_functions import get_text, get_postback
from spell_correct import correct

with open("db/database.json") as f:
    db = json.load(f)

with open("db/mapping.json") as map_file:
    mapping = json.load(map_file)

with open('db/hello-sorry.json') as f:
    msgs = json.load(f)
    hello_msgs = msgs["hello"]
    sorry_msgs = msgs["sorry"]

MESS = {
    "date": '01-01-2018',
    "breakfast": "breakfast",
    "lunch": "lunch",
    "dinner": "dinner"
}

NEUTRAL_WORDS = [
    "lol",
    "ok",
    "lite",
    "no",
    "sorry",
    "phoda",
    "cool",
    "great",
    "fine",
    "alright",
    "awesome",
    "good"]


def sort_query(msg_text, sender_id):
    message_pack = None

    if msg_text in NEUTRAL_WORDS:
        return None

    msg_list = msg_text.split()

    if "hello" in msg_list:
        name = get_name(sender_id)
        message_pack = say_hello(name)

    for meal in ["lunch", "dinner", "breakfast"]:
        if meal in msg_list:
            if 'tomorrow' in msg_list:
                message_pack = get_text(get_meal(meal, tomorrow=True))
            else:
                message_pack = get_text(get_meal(meal))

    if not message_pack:
        message_pack = sort(msg_list)

    return pack_details(message_pack, sender_id)


def sort(msg_list, database=db, level=0):
    """
    Search for every word of msg_list (user's message) in the entire
    database dict (including subdicts),
    if word is found:

    if not found:
        return sorry message.

    Arguements:
    msg_list - user's message
    name - user's name (for sorry message)
    database - database to look for words
    level - recursion level
    kiy - .
    """

    for word in msg_list:
        for key, value in database.items():
            if key == word:
                if isinstance(value, dict):
                    message_pack = sort(msg_list, value, level + 1)
                else:
                    message_pack = value

                return message_pack

    if level:
        postback_msg_value = [" ".join(msg_list) + " " + x for x in database]
        postback_title = [x for x in database]
        return get_postback(postback_msg_value, postback_title)
    else:
        return say_sorry()


def pack_details(datas, recipient_id):
    for data in datas:
        data["recipient"] = {
            "id": recipient_id
        }
        data["messaging_type"] = "RESPONSE"

    return datas


def get_name(sender_id):
    """ Get user's name, if nothing is found, return empty string. """

    r = requests.get("https://graph.facebook.com/v2.6/" + sender_id +
                     "?fields=first_name&access_token=" +
                     os.environ["PAGE_ACCESS_TOKEN"])

    if "first_name" in json.loads(r.text):
        return json.loads(r.text)["first_name"]
    else:
        return ''


def clean_text(text):
    text = text.lower()
    text = text.replace("'s", '')
    text = re.sub(':.', ' ', text)  # Remove instances of emoji
    text = re.sub('\W', ' ', text).strip()  # Remove any other non alphanumeric
    text_list = text.split(' ')
    spell_correct_list = correct(text_list)
    map_list = map_text(spell_correct_list)

    return " ".join(map_list)


def map_text(message_list):
    """ Map words to their dictionary counterpart """
    for word in message_list:
        if word in mapping:
            message_list.remove(word)
            message_list.insert(0, mapping[word])
    return message_list


def say_hello(name):
    """ Hello message with randomized words along with name. """
    hello_msg = random.choice(hello_msgs)
    hello_msg[0] = hello_msg[0].replace('<USERNAME>', name)
    return get_text(hello_msg)


def say_sorry():
    """ sorry message with randomized words. """
    return get_text(random.choice(sorry_msgs))


def get_meal(mealtype, tomorrow=False):
    """ Get today's meal. mealtype: breakfast / lunch / dinner. """
    now = datetime.datetime.now(
        pytz.timezone(
            'Asia/Kolkata')).date(
    )
    if tomorrow:
        now += datetime.timedelta(days=1)
    now = now.strftime(
                '%d-%m-%Y')

    if now != MESS['date']:
        try:
            with open('db/menu/' + now + ".json") as json_data:
                today = json.load(json_data)
        except:
            return "<Sorry, Menu will be updated by tonight>"

        MESS['date'] = now

        prefix = 'today\'s'
        if tomorrow:
            prefix = 'tomorrow\'s'

        MESS["lunch"] = f"{prefix} lunch:\n" + "\n".join(today["lunch"])
        MESS["breakfast"] = f"{prefix} breakfast:\n" + \
            "\n".join(today["breakfast"])
        MESS["dinner"] = f"{prefix} dinner:\n" + "\n".join(today["dinner"])

    return MESS[mealtype]
