def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    if len(word) == 0:
        # print("Cannot enter empty string.")
        return None
    # elif len(word) == 2:
    #     return first(word) == last(word)
    else:
        is_palindrome(middle(word))
        return first(word) == last(word)


word = "redivider", "noon", "ab", "a", "moon", "string", ""
# word = ""         # doesn't work with empty string
# for i in word:
#     print(i)
#     print("first:   ", first(i))
#     print("last:    ", last(i))
#     print("middle:  ", middle(i))

for i in word:
    print(i, "is palindrome: ", is_palindrome(i))
