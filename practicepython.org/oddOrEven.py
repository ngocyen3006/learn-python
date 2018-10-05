def oddevenNumer(n):
    if n % 4 == 0:
        return 0
    if n % 2 == 0:
        return 1
    else:
        return -1


def result(n):
    ans = oddevenNumer(n)
    if ans == 0:
        print("{} is a multiple of 4".format(n))
    if ans == 1:
        print("{} is an even number".format(n))
    else:
        print("{} is an odd number".format(n))


n = int(input())
result(n)
