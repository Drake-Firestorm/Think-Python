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


def interlock(t, word, skip):
    for i in range(skip+1):
        inter = word[i::1+skip]
        if not in_bisect(t, inter):
            return False
    return True


def wordlist():
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


t = wordlist()
skip = 1
for word in t:
    if interlock(t, word, skip):
        print(word, word[::1 + skip], word[1::1 + skip], word[2::1 + skip])
