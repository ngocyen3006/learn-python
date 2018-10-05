import unittest
from stringLists import isPalinrome


class TestIsPalindromeString(unittest.TestCase):
    def test_is_a_palindrome(self):
        string = ["abcdcba", "123454321", "1", "@_@"]
        for s in string:
            self.assertTrue(isPalinrome(s))

    def test_is_not_a_palindrome(self):
        string = ["abcd", "54687", "@#$"]
        for s in string:
            self.assertFalse(isPalinrome(s))


if __name__ == '__main__':
    unittest.main()
