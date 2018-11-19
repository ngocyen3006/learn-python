class Date:
    '''Represents the date of year'''


def is_leap(year):
    '''Check year is leap year or not'''
    leap = False

    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        leap = True

    return leap


def print_date(d):
    print(f"{d.month:02d}/{d.day:02d}/{d.year:04d}")


def increment_date(d, n):
    loop = True
    d.day += n
    cal1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    cal2 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    while loop:
        if is_leap(d.year):
            cal = cal2
        else:
            cal = cal1
        try:
            while d.day > cal[d.month]:
                d.day -= cal[d.month]
                d.month += 1
        except KeyError:
            d.month = 1
            d.year += 1
        if d.day < cal[d.month]:
            loop = False
    return d


if __name__ == '__main__':
    d = Date()
    d.day = 15
    d.month = 1
    d.year = 2016
    print_date(d)
    n = 390
    res = increment_date(d, n)
    print_date(res)
