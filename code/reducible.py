def make_word_dict():
    """
    Reads a word list and returns a word dictionary.

    :return: dictionary with words as keys
    """
    fin = open("words.txt")
    d = dict()
    for line in fin:
        word = line.strip().lower()
        d[word] = d.get(word, 0)
    for letter in ["a", "i", ""]:
        d[letter] = letter
    return d


def children(word, word_dict):
    """
    Returns list of all words that can be formed by removing one letter.

    :param word: string
    :param word_dict: dictionary with words as keys
    :return: list of strings
    """
    li = list()
    for i in range(len(word)):
        child = str(word[:i] + word[i+1:])
        if child in word_dict:
            li.append(child)
    return li


memo = dict()
memo[""] = [""]


def is_reducible(word, word_dict):
    """
    Returns list of all reducible children of the word.

    Also updates memo dictionary with the reducible children

    A string is reducible if it has at least one child that is
    reducible.  The empty string is also reducible.

    :param word: string
    :param word_dict: dictionary with words as keys
    :return: list of strings
    """
    if word in memo:
        return memo[word]

    li = children(word, word_dict)
    red_child = list()
    for child in li:
        if is_reducible(child, word_dict):
            red_child.append(child)
    memo[word] = red_child
    return red_child


def all_reducible(word_dict):
    """
    Return list of all reductible words in the dictionary.

    :param word_dict: dictionary with words as keys
    :return: list of strings
    """
    li = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            li.append(word)
    return li


def print_trail(word):
    """
    Print sequence of words which reduced this word to empty string.
    If more than one trail, it chooses the first.

    :param word: string
    :return: None
    """
    if len(word) == 0:
        return
    print(word, end=" ")
    red_child = is_reducible(word, word_dict)
    print_trail(red_child[0])


def print_longest_words(word_dict):
    """
    Finds the longest reducible words and prints them.

    :param word_dict: dictionary with words as keys
    :return: None
    """
    reducible = all_reducible(word_dict)
    reducible.sort(key=len, reverse=True)
    for word in reducible[:10]:
        print_trail(word)
        print("\n")


word_dict = make_word_dict()
print_longest_words(word_dict)
