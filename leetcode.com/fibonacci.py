# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

def fib(N):
    f0 = -1
    f1 = 1
    f = 0
    for i in range(N + 1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f
