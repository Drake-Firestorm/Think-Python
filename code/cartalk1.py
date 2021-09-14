def consecutive(word):
    word = word.lower()
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return i
    return -1


def is_three_consecutive(word):
    loc = 0
    while loc < len(word):
        word = word[loc:]
        if consecutive(word[loc:]) == -1:
            return False

        loc = consecutive(word)
        if 0 == consecutive(word[loc+2:]) == consecutive(word[loc+4:]):
            return True
        loc = loc + 1


fin = open("words.txt")
for line in fin:
    word = line.strip()
    if is_three_consecutive(word):
        print(word)
