# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

import math


def fib2(N):
    f0 = -1
    f1 = 1
    f = 0
    for i in range(N + 1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f


def fib(N):
    if N < 2:
        return N
    f = (1 / math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2) ** N) - (((1 - math.sqrt(5) / 2) ** N)))
    return round(f)
