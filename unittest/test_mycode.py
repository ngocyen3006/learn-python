import unittest
from mycode import checkPass


class TestCheckPassword(unittest.TestCase):
    def test_checkPassword_too_short(self):
        self.assertFalse(checkPass("Ac8"))
        self.assertFalse(checkPass("a"))

    def test_checkPassword_not_contain_lowercase(self):
        self.assertFalse(checkPass("ASBH1223"))

    def test_checkPassword_not_contain_uppercase(self):
        self.assertFalse(checkPass("ahfuiehkfh148"))

    def test_checkPassword_not_contain_digit(self):
        self.assertFalse(checkPass("fhahfAADNFHUH"))

    def test_checkPassword_is_strong(self):
        self.assertTrue(checkPass("Ahfhkeu8924"))
        self.assertTrue(checkPass("ssffABC562"))


if __name__ == '__main__':
    unittest.main()
