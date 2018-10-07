import unittest
from fibonacci import fibList


class TestFibonacci(unittest.TestCase):
    def test_is_a_fibonacci_list(self):
        self.assertEqual(fibList(2), [1, 1])
        self.assertEqual(fibList(3), [1, 1, 2])
        self.assertEqual(fibList(5), [1, 1, 2, 3, 5])
        self.assertEqual(fibList(1), [1])
        self.assertEqual(fibList(0), [])

    def test_is_not_fibonacci_list(self):
        self.assertNotEqual(fibList(2), [1, 3])
        self.assertNotEqual(fibList(3), [1, 2, 3])
        self.assertEqual(fibList(-1), None)


if __name__ == '__main__':
    unittest.main()
