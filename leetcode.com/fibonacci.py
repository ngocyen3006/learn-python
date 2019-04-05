# https://leetcode.com/problems/fibonacci-number/

def fib(N):
    if N < 2:
        return N
    return fib(N - 1) + fib(N - 2)
