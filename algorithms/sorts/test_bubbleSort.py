import unittest
from bubbleSort import sort


class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(sort([2, 3, 1, 6, 7, 5, 4, 2]), [1, 2, 2, 3, 4, 5, 6, 7])
        self.assertEqual(sort([]), [])
        self.assertEqual(sort([0, 1, 5, 3, 1, 2, 1]), [0, 1, 1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
