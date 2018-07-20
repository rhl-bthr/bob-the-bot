from store_data import *

master_dict = []

def update(dictionary):
    for key, value in dictionary.items():
        master_dict.append(key)
        if isinstance(value, dict):
            update(value)


if(__name__ == "__main__"):
    update(db)
    update(mapping)
    master_list = list(set(master_dict))
    with open('../db/dictionary.txt', 'w') as f:
        for word in master_list:
            f.write(word)
            if word != master_list[-1]:
                f.write("\n")
