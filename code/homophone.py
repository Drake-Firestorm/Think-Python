from pronounce import read_dictionary

def worddict():
    fin = open("words.txt")
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = d.get(word, 0)
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


words = worddict()
pron_dict = read_dictionary()
inverse_pron_dict = invert_dict(pron_dict)

five_letter_words = words
# five_letter_words = list()
# for word in words:
#     if len(word) == 5:
#         five_letter_words.append(word)


for word in five_letter_words:
    if word in pron_dict:
        pron = pron_dict.get(word)
    else:
        continue
    drop_first = word[1:]
    drop_second = word[0] + word[2:]
    if word in inverse_pron_dict.get(pron) and drop_first in inverse_pron_dict.get(pron) and drop_second in inverse_pron_dict.get(pron):
        print(pron, word, drop_first, drop_second)
