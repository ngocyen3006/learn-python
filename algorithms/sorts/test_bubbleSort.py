import unittest
from bubbleSort import bubbleSort


class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        a = [2, 3, 1, 6, 7, 5, 4]
        b = []
        c = [0, 1, 5, 3, 1, 2, 1]
        bubbleSort(a)
        bubbleSort(b)
        bubbleSort(c)
        self.assertEqual(a, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(b, [])
        self.assertEqual(c, [0, 1, 1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
