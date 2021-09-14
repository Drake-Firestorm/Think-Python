import random

def has_duplicates(t):
    s = sorted(t)
    s.sort()
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return True
    return False


def generate_birthday(student_count):
    x = []
    for i in range(student_count):
        x.append(random.randint(1, 365))
    return x


def count_matches(student_count, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = generate_birthday(student_count)
        count += has_duplicates(t)
    return count


simm_count = 1000
stud_count = 23
print("No. of simulations:", simm_count)
print("No. of students:", stud_count)
print("No. of simulations with birthday's repeated:", count_matches(stud_count, simm_count))
