# # 1 -                   last 4 digits were palindromic                  e.g. 3-1-5-4-4-5
# # 2 - 1 mile later -    last 5 numbers were palindromic                 e.g. 3-6-5-4-5-6
# # 3 - 1 mile later -    middle 4 out of 6 numbers were palindromic
# # 3 - 1 mile later -    all 6 were palindromic


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


def is_palindrome(word):
    return is_reverse(word, word)


def is_number_palindrome(number, digits, start):
    """
    Return if the selected digits from start in the number are a palindrome

    :param number:
    :param digits:
    :param start:
    :return:
    """
    number = str((number // 10**start) % 10**digits).rjust(digits, "0")
    return is_palindrome(number)


for i in range(10**5, 10**6 - 4):
    if is_number_palindrome(i, 4, 0) and is_number_palindrome(i+1, 5, 0) and is_number_palindrome(i+2, 4, 1) and is_number_palindrome(i+3, 6, 0):
        print(i)
