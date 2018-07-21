
def get_file(paths, file_type):
    """get files for messages formatted according to API (json). """

    if not isinstance(paths, list):
        paths = [paths]

    data = []
    for path in paths:
        data.append({
            "message": {
                "attachment": {
                    "type": file_type,
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

POSTBACK_DEFAULT = "Here's are some things to choose from:"


def get_postback(postback_value, postback_title, append_text=POSTBACK_DEFAULT):
    """
    Get postback formatted according to API (json).

    Arguements:
    postback_value -
    postback_title - titles for data (for buttons)
    types - type of data (phone number/contact/link/list)
    append_text - text to be appended to specify type of data given by BOB.

    Returns:
    formatted message with required fields.
    """
    data, buttons = [], []

    if not isinstance(postback_value, list):
        postback_value = [postback_value]
    if not isinstance(postback_title, list):
        postback_title = [postback_title]
    for x in range(len(postback_value)):
        buttons.append({
            "type": "postback",
            "title": postback_title[x],
            "payload": postback_value[x]
        })

    # buttons are grouped in 3s and stored in lists
    # [[b1,b2,b3], [b4,b5,b6] [b7,b8,b9], ... ]
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


def get_url(entity, subject):
    data = [{
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Here's the link:",
                    "buttons": {
                        "type": "web_url",
                        "title": subject,
                        "url": entity
                    }
                }
            }
        }
    }]
    return data


def get_text(texts, entity=None):
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
    data = []
    if entity:
        texts = [entity + ":\n" + text for text in texts]
    for text in texts:
        data.append({
            "message": {
                "text": text,
            }
        })
    return data
