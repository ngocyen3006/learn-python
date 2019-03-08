# https://leetcode.com/problems/reverse-integer/
def reverse(x):
    y = abs(x)
    n = 0
    while y > 0:
        n = n * 10 + y % 10
        y = y // 10
    if n > 2 ** 31 or x == 0:
        return 0
    n = n * x // abs(x)
    return n


if __name__ == "__main__":
    n = -123
    print(reverse(n))
    print("-" * 20)
    n = 1534236469
    print(reverse(n))
    print("-" * 20)
    n = 123
    print(reverse(n))
    print("-" * 20)
    n = 1563847412
    print(reverse(n))
    print("-" * 20)
