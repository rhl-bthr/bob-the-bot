""" Store all keys from db and mapping to db/dictionary.txt. """

from store_data import db
from database import mapping
master_dict = []


def update(dictionary):
    """
    Traverse the entire dictionary (inclding all subdictionaries)
    and store all keys in master_dict.
    """
    for key, value in dictionary.items():
        master_dict.append(key)
        if isinstance(value, dict):
            update(value)

if __name__ == "__main__":
    update(db)
    update(mapping)

    # remove duplicates
    master_list = list(set(master_dict))

    # store all words from master dictionary to dictionary.txt
    with open('db/dictionary.txt', 'w') as f:
        for word in master_list:
            f.write(word)
            if word != master_list[-1]:
                f.write("\n")
