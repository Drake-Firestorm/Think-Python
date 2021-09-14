import time


def words_to_list_fun():
    start = time.time()
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return time.time() - start


def words_to_list_sym():
    start = time.time()
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t = t + [word]
    return time.time() - start


print("Time using append:",  words_to_list_fun())
print("Time using +:",  words_to_list_sym())
