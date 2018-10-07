# https://www.hackerrank.com/challenges/python-string-formatting/problem

n = int(input())


def print_formatted(number):
    width = len('{0:b}'.format(number))

    for i in range(1, number + 1):
        # decNum = i  # decimal i
        # octNum = oct(i)[2:]  # octal i
        # hexNum = hex(i)[2:]  # hexadecimal i
        # binNum = bin(i)[2:]  # binary i
        print(
            "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


print_formatted(n)
