def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def has_duplicates(t):
    hist = histogram(t)
    inverse = invert_dict(hist)
    for i in range(2, 2**len(inverse)):
        if i in inverse:
            return True
    return False


t = [1, 2, 3]
print(t, has_duplicates(t))
t.append(1)
print(t, has_duplicates(t))
