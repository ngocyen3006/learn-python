# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

from math import sqrt, floor


def isPrime(n):
    if type(n).__name__ != 'int':
        return False

    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    upper_bound = floor(sqrt(n))
    for i in range(2, upper_bound + 1):
        if n % i == 0:
            return False

    return True
