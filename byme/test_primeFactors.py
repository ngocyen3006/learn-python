import unittest
from primeFactors import primefactors, listPrime, isPrime
from prime_factors import primefactors
import random


def checkDict(dict):
    result = 1
    for i in dict.keys():
        if isPrime(i):
            result = result * (i ** dict[i])
    return result


class TestPrimeFactors(unittest.TestCase):
    def test_n_is_1(self):
        self.assertEqual(primefactors(1), {1: 1})

    def test_n_lesser_1(self):
        arr = [-1, 0]
        for i in arr:
            self.assertEqual(primefactors(i), -1)

    def test_n_is_not_a_prime_number(self):
        n = random.randint(2, 10000)
        self.assertEqual(checkDict(primefactors(n)), n)


if __name__ == '__main__':
    unittest.main()
