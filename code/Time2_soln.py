class Time:
    """Represents the time of day.

    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
        Initialize a Time object.

        :param hour: integer
        :param minute: integer
        :param second: integer
        """
        self.seconds = hour*60*60 + minute*60 + second

    def __str__(self):
        """
        Return a string representation of the time.

        :return: string
        """
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return "%.2d:%.2d:%.2d" % (hour, minute, second)

    def __add__(self, other):
        """
        Adds two Time objects or a Time object and a number.

        :param other: Time object or number of seconds
        :return: Time object
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """
        Adds two Time objects or a Time object and a number.

        :param other: Time object or number of seconds
        :return: Time object
        """
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def print_time(self):
        """
        Print Time in Hour:Minute:Second

        :return: None
        """
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        print('%.2d:%.2d:%.2d' % (hour, minute, second))

    def time_to_int(self):
        """
        Convert time to seconds.

        :return: Integer
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        """
        Add seconds to time.

        :param seconds:
        :return: Time Object
        """
        seconds += self.seconds
        return int_to_time(seconds)

    def is_after(self, other):
        """
        Check if t1 follows t2 chronologically.

        :param other: Time object
        :return: Boolean
        """
        return self.seconds > other.seconds


def int_to_time(seconds):
    """
    Convert seconds  to Time.

    :param seconds: integer
    :return: Time object
    """
    time = Time()
    time.seconds = seconds
    return time


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    #end = start.increment(1337, 460)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == "__main__":
    main()