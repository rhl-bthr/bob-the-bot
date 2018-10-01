# Handle requests to and from facebook API and heroku server

import os
import json
from query_sort import clean_text, sort_query

msg_text = input('Message: ')
sender_id = "1234"
msg_text = clean_text(msg_text)
print(f'cleaned Message: {msg_text}\n')
send_packets = sort_query(msg_text, sender_id)
for packet in send_packets:
    try:
        print(packet['message']['text'])
    except:
        print(f'\n-----------\n{packet}\n-----------------\n')
