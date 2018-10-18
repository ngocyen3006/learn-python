import unittest
from binarySearch import binarySearch


class TestSearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(binarySearch([], 1), -1)

    def test_search_found(self):
        a = [i for i in range(20)]
        self.assertEqual(binarySearch(a, 5), 5)

    def test_search_not_found(self):
        a = [i for i in range(20)]
        self.assertEqual(binarySearch(a, 20), -1)


if __name__ == '__main__':
    unittest.main()
