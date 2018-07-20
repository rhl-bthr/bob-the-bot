""" Main program that handles requests to and from facebook API and heroku server. """

import os
import json
import requests
import re
from flask import Flask, request

from query_sort import *
from spell_correct import correct

app = Flask(__name__)

semantic_json = json.load(open('db/semantic_words.json'))

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get(
            "hub.challenge"):
        if not request.args.get(
                "hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Err: 404, you came to the wrong place <br> \
            Visit <a href=https://www.facebook.com/ChatbotBOB>BOB's \
            facebook page</a>", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for msg_event in entry["messaging"]:
                sender_id = msg_event["sender"]["id"]
                if isinstance(msg_event, list):
                    msg_event = msg_event[0]
                if "postback" in msg_event:
                    msg_text = msg_event["postback"]["payload"].lower(
                    )
                elif "text" in msg_event["message"]:
                    msg_text = msg_event["message"]["text"].lower(
                    )
                else:
                    return "ok", 200
                msg_text = msg_text.replace("'s", '')
                msg_text = re.sub(':.', ' ', msg_text)
                msg_text = re.sub('\W', ' ', msg_text).strip()
                if msg_text:
                    message_pack = None
                    if msg_text in semantic_json['neutral']:
                        continue
                    if msg_text in semantic_json['happy']:
                        message_pack = getText("Happy to help :D")

                    if not message_pack:
                        message_list = msg_text.split(' ')
                        correct_msg = correct(message_list)
                        message_list = map_text(correct_msg)
                        name = getName(sender_id)
                        message_pack = sort(message_list, name)
                    data = unpack(message_pack, sender_id)
                    send_message(data)

    return "ok", 200


def send_message(datas):
    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }

    for data in datas:
        data = json.dumps(data)
        print('d:', data)
        r = requests.post(
            "https://graph.facebook.com/v2.6/me/messages",
            params=params,
            headers=headers,
            data=data)

if __name__ == '__main__':
    app.run(debug=True)
