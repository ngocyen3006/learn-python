# https://www.hackerrank.com/challenges/string-validators/
from functools import reduce


def anyMatch(test, s):
    return reduce((lambda x, y: x or test((y))), s, False)


if __name__ == '__main__':
    s = input()

    # Method 1
    # check a string is contain alphanumeric character
    print(anyMatch(lambda x: x.isalnum(), s))
    # check a string is contain  alphabetical character
    print(anyMatch(lambda x: x.isalpha(), s))
    # check a string  is contain digit character
    print(anyMatch(lambda x: x.isdigit(), s))
    # check a string is contain lowercase character
    print(anyMatch(lambda x: x.islower(), s))
    # check a string is contain uppercase character
    print(anyMatch(lambda x: x.isupper(), s))

    # Method 2
    print("---------------------------------")
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
