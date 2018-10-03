import unittest
from prime import is_prime


class TestIsPrime(unittest.TestCase):
    def test_is_not_prime(self):
        test_cases_fail = [100, 0, -1, 1, 1.0]
        for i in test_cases_fail:
            self.assertFalse(is_prime(i), "{} is prime".format(i))

    def test_is_prime(self):
        test_cases = [2, 3, 5, 7, 11, 13, 17, 19, 1123]
        for i in test_cases:
            self.assertTrue(
                is_prime(i), "expect {} is prime, but it is not".format(i))

    def test_input_is_not_number(self):
        test_cases_not_numbers = [
            "abc",
            "1",  # check if python auto convert string into number
            None,
            unittest,  # a module, not a number
        ]
        for i in test_cases_not_numbers:
            self.assertFalse(is_prime(i))


if __name__ == '__main__':
    unittest.main()
