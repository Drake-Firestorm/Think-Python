# Method 1: using in_reverse()
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1

    return True


def reverse_pair1(t):
    for i in range(len(t)):
        for j in range(i, len(t)):
            if is_reverse(t[i], t[j]):
                print(t[i], t[j])


# Method 2: using in_bisect()
def in_bisect(t, target):
    i = int(len(t) / 2)
    if len(t) == 0:
        return False
    elif target < t[i]:
        return in_bisect(t[:i], target)
    elif target > t[i]:
        return in_bisect(t[i+1:], target)
    else:
        return True


def reverse_pair2(t):
    for word in t:
        rev_word = word[::-1]
        if in_bisect(t, rev_word):
            print(word, rev_word)


def wordlist():
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


# reverse_pair1(wordlist())
reverse_pair2(wordlist())

# Method 2 is much faster since it cuts down the search list each time in half.
