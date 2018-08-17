n = int(input())


def fib(n):
    if(n == 0 or n == 1):
        return n

    a = 0
    b = 1

    i = 2
    while(i <= n):
        i = i + 1
        S = a + b
        a = b
        b = S

    return b


re = fib(n)
print(re)
