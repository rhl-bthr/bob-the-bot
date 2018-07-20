""" Manipulate user queries. """

from store_data import db
from database import mapping, sayHello, saySorry, getText, getMeal, getNum
import requests


def map_text(message_list):
    """ Try to replace common unknowns words with known words from db/mapping.json.  """
    for word in message_list:
        if word in mapping:
            message_list.remove(word)
            message_list.insert(0, mapping[word])
    return message_list


def getName(sender_id):
    """ Get user's  name from facebook API, if nothing is found, return empty string. """
    try:
        r = requests.get(
            "https://graph.facebook.com/v2.6/" +
            sender_id +
            "?fields=first_name&access_token=" +
            os.environ["PAGE_ACCESS_TOKEN"])
        print(r.text)
        if "first_name" in json.loads(r.text):
            name = json.loads(r.text)["first_name"]
        return name
    except:
        return ''


def sort(msg_list, name, database=db, level=0, kiy=None):
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
    if "hello" in msg_list:
        message_pack = sayHello(name)
        return message_pack

    for word in msg_list:
        for key, value in database.items():
            if key == word:
                if isinstance(value, dict):
                    message_pack = sort(msg_list, name, value, level + 1, key)
                elif isinstance(value, str):
                    return getText("Today's " + value + "\n" + getMeal(value))
                else:
                    message_pack = value
                return message_pack

    if level:
        return getNum([
            " ".join(msg_list) + " " + x for x, __ in database.items()], [
            x for x, __ in database.items()], "postback", kiy.upper() + " options:")
    else:
        return saySorry(name)


def unpack(datas, recipient_id):
    for data in datas:
        data["recipient"] = {
            "id": recipient_id
        }
        data["messaging_type"] = "RESPONSE"

    return datas
