from pprint import pprint
import most_frequent


def read_wordlist(filename):
    wordlist = list()
    fin = open(filename)
    for line in fin:
        word = line.strip()
        wordlist.append(word)
    return wordlist


def anagram_dict(wordlist):
    d = dict()
    for word in wordlist:
        key = tuple(sorted(word))
        d.setdefault(key, []).append(word)
    return d


def word_anagram(word, anagram_dict):
    key = tuple(sorted(word))
    return anagram_dict.get(key, [word])


def anagrams(anag_dict):
    # # Part 1.
    # for key, anagram_list in anag_dict.items():
    #     if len(anagram_list) > 1:
    #         print(anagram_list)
    # Part 2
    for key in sorted(anag_dict, key=len, reverse=True):
        # print(key)
        if len(anag_dict.get(key)) > 1:
            print(len(anag_dict.get(key)), anag_dict.get(key))


def max_bingo(anag_dict):
    d = dict()
    for key in sorted(anag_dict, key=len, reverse=True):
        if len(key) == 8:
            d[key] = len(anag_dict.get(key))
    d = most_frequent.inverse_dict(d)
    return d.get(max(d))


# test words
w = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',  'retainers', 'ternaries',  'generating', 'greatening', 'resmelts', 'smelters', 'termless']

# f = "words.txt"
# w = read_wordlist(f)

d = anagram_dict(w)
# pprint(d)
# anagrams(d)

# most_bingos = max_bingo(d)
# print(most_bingos, d.get(most_bingos[0]))
