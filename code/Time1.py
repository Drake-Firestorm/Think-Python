from datetime import datetime

class Time:
    """Represents the time of the day.

    attributes: hour, minute, second
    """


def print_time(time):
    """
    Print time in the form hour:minute:second

    :param time: Time object
    :return: None
    """
    print("%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second))


def is_after(t1, t2):
    """
    Check if t1 follows t2 chronologically.

    :param t1: Time object
    :param t2: Time object
    :return: Boolean
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)
    # alternate
    # t1_seconds = t1.hour*60*60 + t1.minute*60 + t1.second
    # t2_seconds = t2.hour*60*60 + t2.minute*60 + t2.second
    # return t1_seconds > t2_seconds


def add_time(t1, t2):
    """
    Returns sum of two times.

    :param t1: Time object
    :param t2: Time object
    :return: Time object
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


def increment(time, seconds):
    """
    Add seconds to time.

    :param time: Time object
    :param seconds: integer
    :return: Time object
    """
    return add_time(time, int_to_time(seconds))


def time_to_int(time):
    """
    Convert time to seconds.

    :param time: Time object
    :return: integer
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    """
    Convert seconds  to Time.

    :param seconds: integer
    :return: Time object
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def valid_time(time):
    """
    Checks if the time is valid.

    :param time: Time object
    :return: Boolean
    """
    if time.hour <0 or time.minute < 0 or time.second <0:
        return False
    if time.minute >=60 or time.second >= 60:
        return False
    return True


def mul_time(time, multiplier):
    """
    Multiple time with a number.

    :param time: Time object
    :param multiplier: float
    :return: Time object
    """
    assert valid_time(time)
    seconds = time_to_int(time)
    return int_to_time(seconds * multiplier)


def avg_pace(finish_time, distance):
    """
    Returns average pace per mile (time per mile).

    :param finish_time: Time object
    :param distance: float
    :return: Time object
    """
    assert valid_time(finish_time)
    return mul_time(finish_time, 1/distance)


def days_till_birthday(birthday):
    """
    Prints current age and returns days till next birthday

    :param birthday: Time object
    :return: integer
    """
    assert valid_time(birthday)
    today = datetime.now()
    age = today - birthday
    age = age.days // 365
    print("Age(in years) :", age)

    next_birthday = datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

    days_till = next_birthday - datetime.now()
    return days_till.days


def double_day(birthday_1, birthday_2, n):
    """
    Returns the day one person is n time older than another.

    :param birthday_1: Time object
    :param birthday_2: Time object
    :param n: integer
    :return: Time object
    """
    assert valid_time(birthday_1) and valid_time(birthday_2)
    b1 = max(birthday_1, birthday_2)
    b2 = min(birthday_1, birthday_2)
    print(b1, b2)
    delta = b1 - b2
    return b1 + (delta / (n-1))


def datetime_exercises():
    """Exercise solutions"""

    # print today's day of week
    print(datetime.now().weekday())

    # days till next birthday
    print(days_till_birthday(datetime(1967, 5, 2)))

    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print('Double Day', end=' ')
    print(double_day(b1, b2, 2))


if __name__ == "__main__":
    t = Time()
    t.hour = 11
    t.minute = 59
    t.second = 30

    t2 = Time()
    t2.hour = 11
    t2.minute = 59
    t2.second = 31

    print_time(t)
    print(is_after(t, t2))
    print_time(add_time(t, t2))
    print_time(increment(t, 3723))
    print_time(mul_time(t, 2))
    print_time(avg_pace(t, 10))

    datetime_exercises()
