"""
Module to spell check words.

Use correct() function (from spell_correct import correct)
Arguements - list of words to be corrected
Returns - list of corrected words.
"""


dictionary = open('../db/dictionary.txt').read()
common_dict = open('../db/commondict.txt').read()
WORDS = (dictionary + common_dict).split("\n")


def correct(word_list):
    """
    Primary function to spell correct a word.

    Only corrects words that are > 4 in length.
    """
    corrected_list = []
    for word in word_list:
        if len(word) > 4:
            corrected_list.append(mini_correction(word))
        else:
            corrected_list.append(word)
    return corrected_list


def mini_correction(word):
    try:
        return (known([word]) + known(edits1(word)))[0]
    except:
        return ''


def known(words):
    """
    Return the subset of `words` that appear in the dictionary of WORDS.

    returns words in 'words' that are a part of the main dictionary - WORDS
    """
    return list(set(w for w in words if w in WORDS))


def edits1(word):
    """Return all edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)
