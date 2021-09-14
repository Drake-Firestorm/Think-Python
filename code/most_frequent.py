def inverse_dict(d):
    """
    Invert dict by interchanging key-value pair and combining all values for the new key in a list.
    Tested with d = str-int key-value pair

    :param d: dict to be inverted
    :return:  inverted dict
    """
    d2 = dict()
    for index, element in d.items():
        element, index = index, element
        d2.setdefault(index, []).append(element)
    return d2


def sorted_dict(d, rev=False):
    """
    Sort a dict based on keys. Default is ascending.

    :param d: dict to be sorted
    :param rev: reverse flag. defaults to False
    :return: sorted dict
    """
    return dict(sorted(list(d.items()), reverse=rev))


def most_frequent(s):
    """
    Prints count and list of letters in  the given string.

    :param s: string
    :return: None
    """
    d = dict()
    for letter in s:
        d[letter] = d.setdefault(letter, 0) + 1
    d = inverse_dict(d)
    d = sorted_dict(d, True)
    return d


# string = "toople"
# most_frequent(string)

string = open("emma.txt", encoding='utf-8').read()
d = most_frequent(string)
# for count, letter in d.items():
#     print(count, letter)
