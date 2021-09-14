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
    number = str((number // 10**start) % 10**digits).zfill(digits)
    return is_palindrome(number)


for age_diff in range(1, 100):
    counter = 0
    current_age = 0
    for age in range(1, 100):
        counter = counter + is_reverse(str(age).zfill(2), str(age + age_diff).zfill(2))
        if counter == 6 and current_age == 0:
            current_age = age
        if counter > 8:
            break
    if counter == 8:
        print("Current age:", current_age, "\tMother's Age:", current_age + age_diff)
