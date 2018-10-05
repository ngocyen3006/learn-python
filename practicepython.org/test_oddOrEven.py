import unittest
from oddOrEven import oddevenNumer


class TestOddOrEvenNumber(unittest.TestCase):
    def test_is_odd_number(self):
        oddNum = [1, 3, 5, 11, 21, 37, -3]
        for i in oddNum:
            self.assertEqual(oddevenNumer(i), -1)

    def test_is_even_number(self):
        evenNum = [-2, 2, 98, 10]
        for i in evenNum:
            self.assertEqual(oddevenNumer(i), 1)

    def test_number_is_a_multiple_of_four(self):
        multipleFour = [4, 8, 12, 16, 96, 204, 0]
        for i in multipleFour:
            self.assertEqual(oddevenNumer(i), 0)


if __name__ == '__main__':
    unittest.main()
