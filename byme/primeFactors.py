from math import sqrt, floor


def isPrime(x):
    if x <= 1:
        return False

    if x <= 3:
        return True

    upper_bound = floor(sqrt(x))
    for i in range(2, upper_bound + 1):
        if x % i == 0:
            return False

    return True


def listPrime(n):
    arr = []
    upper_bound = floor(sqrt(n))
    for x in range(2, n + 1):
        is_prime = True
        for i in arr:
            if i <= (upper_bound + 1) and x % i == 0:
                is_prime = False
                pass

        if is_prime:
            arr.append(x)

    return arr


def primefactors(n):
    if n < 1:
        return -1
    if n == 1:
        return 1
    if isPrime(n):
        return n
    arr = listPrime(n // 2)
    factors = {}
    while n > 1:
        for i in arr:
            if n % i == 0:
                factors.setdefault(i, 0)
                factors[i] = factors[i] + 1
                n = n / i
    return list(factors.keys())

