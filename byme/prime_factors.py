def primefactors(n):
    if n < 1:
        return -1
    if n == 1:
        return {1: 1}

    factors = {}
    x = 2
    while n > 1:
        if n % x != 0:
            x += 1
            continue
        factors.setdefault(x, 0)
        factors[x] = factors[x] + 1
        n = n / x
    return factors
