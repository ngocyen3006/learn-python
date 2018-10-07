import unittest
from primeNumber import isPrime


class TestPrimeNumber(unittest.TestCase):
    def test_is_a_prime(self):
        a = [2, 3, 5, 7, 11, 31, 59]
        for i in a:
            self.assertTrue(isPrime(i))

    def test_is_not_prime(self):
        a = [9, 81, 140, 200, -2]
        for i in a:
            self.assertFalse(isPrime(i))

    def test_input_is_not_number(self):
        a = ["a", "1"]
        for i in a:
            self.assertFalse(isPrime(i))


if __name__ == '__main__':
    unittest.main()
