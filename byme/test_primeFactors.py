import unittest
from primeFactors import primefactors


class TestPrimeFactors(unittest.TestCase):
    def test_n_is_a_prime_number(self):
        arr = [2, 3, 7, 11, 71]
        for i in arr:
            self.assertEqual(primefactors(i), i)

    def test_n_is_1(self):
        self.assertEqual(primefactors(1), 1)

    def test_n_lesser_1(self):
        arr = [-1, 0]
        for i in arr:
            self.assertEqual(primefactors(i), -1)

    def test_n_is_not_a_prime_number(self):
        self.assertEqual(primefactors(898), [2, 449])
        self.assertEqual(primefactors(938), [2, 7, 67])
        self.assertEqual(primefactors(780), [2, 3, 5, 13])


if __name__ == '__main__':
    unittest.main()
