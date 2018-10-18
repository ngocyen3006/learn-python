import unittest
import random
from linearSearch import linearSearch


class TestSearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(linearSearch([], 1), -1)

    def test_search_found(self):
        a = [0, 2, 4, 8, 6, 5, 4, 8, 5, 2, 1, 2, 5]
        self.assertEqual(linearSearch(a, 5), 5)

    def test_search_not_found(self):
        a = [i for i in range(20)]
        random.shuffle(a)
        self.assertEqual(linearSearch(a, 20), -1)


if __name__ == '__main__':
    unittest.main()
