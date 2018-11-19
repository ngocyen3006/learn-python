class Time:
    '''represents the time of day.
       attributes: hour, minute, second'''


def print_time(t):
    '''Prints a string representation of the time'''
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")


def is_after(t1, t2):
    '''Returns True if t1 is after t2; false otherwise.'''
    t1 = t1.hour * 3600 + t1.minute * 60 + t1.second
    t2 = t2.hour * 3600 + t2.minute * 60 + t2.second
    return t1 > t2


def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum


if __name__ == "__main__":
    time = Time()
    time.hour = 11
    time.minute = 59
    time.second = 30
    print_time(time)

    t1 = Time()
    t1.hour = 5
    t1.minute = 30
    t1.second = 4

    t2 = Time()
    t2.hour = 4
    t2.minute = 40
    t2.second = 59
    print(is_after(t1, t2))
