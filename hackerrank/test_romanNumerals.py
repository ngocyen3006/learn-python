import unittest
from romanNumerals import checkRomanNumerals


class TestCheckRomanNumerals(unittest.TestCase):
    def test_is_not_Roman_numerals(self):
        self.assertFalse(checkRomanNumerals("a"), "True")
        self.assertFalse(checkRomanNumerals("1"), "True")
        self.assertFalse(checkRomanNumerals("DXXVIIII"), "True")

    def test_input_is_not_string(self):
        self.assertFalse(checkRomanNumerals(5))

    def test_is_a_Roman_numerals(self):
        self.assertTrue(checkRomanNumerals("XXX"))
        self.assertTrue(checkRomanNumerals("CDXXI"))
        self.assertTrue(checkRomanNumerals("CCC"))


if __name__ == '__main__':
    unittest.main()
