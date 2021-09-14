from rotate import rotate_word
import pprint


def pairs_dict(t):
    """Generate all rotated words for each word in the list

    :param t: list of words
    :return: dict with word-rotated word key-value pair
    """
    pairs = dict()
    for word in t:
        for i in range(1, 26):
            rotated_word = rotate_word(word, i)
            pairs.setdefault(word, []).append(rotated_word)
    return pairs


def rotate_pair(pairs, target):
    """Return rotated word for target.

    :param pairs: dict with word-rotated word key value pairs
    :param target: word to search in pairs
    :return: rotated word if found else -1
    """
    for key in pairs:
        # print(target, len(target), key, len(key))
        if len(target) == len(key):
            if target in pairs.get(key):
                return key
    return -1


def wordlist():
    """Generate list of words from words.txt file"""
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


# words = ["aah", "abet", "abjurer", "eel", "hila", "nowhere"]
list_word = wordlist()
dict_pairs = pairs_dict(list_word)
# pprint.pprint(dict_pairs)

for word in list_word:
    pair = rotate_pair(dict_pairs, word)
    # print(word, pair)
    if pair != -1:
        print(word, pair)
