import bisect
import time

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


def in_bisect_fun(t, target):
    i = bisect.bisect_left(t, target)
    if i == len(t):
        return False
    return target == t[i]


def wordlist():
    fin = open("words.txt")
    t = []
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


print("Without Bisect module")
for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print(word, 'in list', in_bisect(wordlist(), word))

print("\n")
print("With Bisect module")
for word in ['aa', 'alien', 'allen', 'zymurgy']:
    print(word, 'in list', in_bisect_fun(wordlist(), word))
