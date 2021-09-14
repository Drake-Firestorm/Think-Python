import anagram_sets_Allen_Downey
import shelve


def store_anagrams(d, filename):
    try:
        shelf = shelve.open(filename)

        for key, values in d.items():
            if len(values) > 1:
                shelf[key] = values
        shelf.close()
    except:
        print("Error storing anagram")
        raise


def read_anagram(word, filename):
    shelf = shelve.open(filename)
    word = "".join(sorted(word.lower()))
    anagrams = list()
    if word in d:
        anagrams = d.get(word)
    else:
        anagrams = -1
    shelf.close()
    return anagrams


if __name__ == "__main__":
    d = anagram_sets_Allen_Downey.all_anagrams("words.txt")
    # store_anagrams(d, "words_anagram")
    print(read_anagram("stop", "words_anagram"))
