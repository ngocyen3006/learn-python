# 204. Count Primes
# https://leetcode.com/problems/count-primes/

# Runtime: 228ms (89.25%)
# Memory: 36.3 MB (5.46%)

def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


if __name__ == '__main__':
    print(countPrimes(999983))