# Handle requests to and from facebook API and heroku server

import os
import json
import requests
from flask import Flask, request
from query_sort import clean_text, sort_query

app = Flask(__name__)

POST_PARAMS = {
    "access_token": os.environ["PAGE_ACCESS_TOKEN"]
}
POST_HEADERS = {
    "Content-Type": "application/json"
}


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
                    msg_text = msg_event["postback"]["payload"]
                elif "text" in msg_event["message"]:
                    msg_text = msg_event["message"]["text"]
                else:
                    return "ok", 200
                msg_text = clean_text(msg_text)

                send_packets = sort_query(msg_text, sender_id)
                send_message(send_packets)

    return "ok", 200


def send_message(send_packets):
    if send_packets:
        for packet in send_packets:
            json_packet = json.dumps(packet)
            requests.post(
                "https://graph.facebook.com/v2.6/me/messages",
                params=POST_PARAMS,
                headers=POST_HEADERS,
                data=json_packet)

if __name__ == '__main__':
    app.run(debug=True)
