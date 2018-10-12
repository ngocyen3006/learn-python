from unittest import TestCase
from maxOfThree import maxOfThree


class TestMaxOfThree(TestCase):
    def test_max_of_three(self):
        self.assertEqual(maxOfThree(1, 5, 2), 5)
        self.assertEqual(maxOfThree("a", "z", "f"), "z")
        self.assertEqual(maxOfThree("", "", ""), "")
        self.assertEqual(maxOfThree(5, 5, 5), 5)

    def test_TypeError(self):
        self.assertEqual(maxOfThree("a", 5, True), None)
