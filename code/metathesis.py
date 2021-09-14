from anagram_sets import anagram_dict
from anagram_sets import read_wordlist

# Method using string
def is_metathesis1(word1, word2):
# # This doesn't work since it ignores multiple conditions
# # e.g. zaffers zaffres, aah aha
# def is_metathesis(word1, word2):
#     mid = int(len(word1)/2)
#     if word1 == word2 or len(word1) != len(word2):
#         return False
#     if mid*2 > 3:
#         if word1[:mid] != word2[:mid] and word1[mid:] != word2[mid:]:
#             return False
#         elif word1[:mid] == word2[:mid] and word1[mid:] != word2[mid:]:
#             return is_metathesis(word1[mid:], word2[mid:])
#         elif word1[:mid] != word2[:mid] and word1[mid:] == word2[mid:]:
#             return is_metathesis(word1[:mid], word2[:mid])
#         else:
#             return True
#     else:
#         if word1[mid] != word2[mid]:
#             return False
#         else:
#             return True
    pass


# solution
def metathesis(d):
    for anagrams in d.values():
        for word in anagrams:
            for target in anagrams:
                if word < target and word_distance(word, target) <= 2:
                    print(word, target)



def word_distance(word1, word2):
    dist = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            dist += 1
    return dist


# test words
# w = ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',  'retainers', 'ternaries',  'generating', 'greatening', 'resmelts', 'smelters', 'termless']

w = read_wordlist("words.txt")
d = anagram_dict(w)

# method 2
metathesis(d)

# # Method 1
# for key in d:
#     metathesis_words = []
#     wordslist = d.get(key)
#     for word in wordslist:
#         if word in metathesis_words:
#             continue
#         for target in wordslist:
#             if is_metathesis1(word, target):
#                 metathesis_words.extend([word, target])
#                 print(word, target)
