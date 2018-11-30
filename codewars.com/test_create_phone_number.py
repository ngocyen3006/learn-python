from unittest import TestCase
from create_phone_number import create_phone_number

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
res_a = "(123) 456-7890"

b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
res_b = "(111) 111-1111"

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
res_c = "(123) 456-7890"

d = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
res_d = "(023) 056-0890"

e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
res_e = "(000) 000-0000"


class TestCreatePhoneNumber(TestCase):
    def test_input_a(self):
        self.assertEqual(res_a, create_phone_number(a))

    def test_input_b(self):
        self.assertEqual(res_b, create_phone_number(b))

    def test_input_c(self):
        self.assertEqual(res_c, create_phone_number(c))

    def test_input_d(self):
        self.assertEqual(res_d, create_phone_number(d))

    def test_input_e(self):
        self.assertEqual(res_e, create_phone_number(e))
