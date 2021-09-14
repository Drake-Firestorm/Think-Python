def rotate_letter(l, n):
    ord_l = ord(l)
    if l.isupper():
        end = ord("Z")
    else:
        end = ord("z")

    if ord_l + n > end:
        n = n - (end - ord_l + 1)
        start = end - 25
    else:
        start = ord_l

    return chr(start + n)


def rotate_word(s, n):
    cypher = ""
    if not s.isalpha():
        print("string should contain only alphabets.")
        return -1
    for letter in s:
        cypher = "".join(cypher + rotate_letter(letter, n))
    return cypher


string = "jolly"
number = -7
print(rotate_word(string, number))
