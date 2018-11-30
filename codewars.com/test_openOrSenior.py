from unittest import TestCase
from openOrSenior import openOrSenior

a = [[45, 12], [55, 21], [19, -2], [104, 20]]
res_a = ['Open', 'Senior', 'Open', 'Senior']

b = [[16, 23], [73, 1], [56, 20], [1, -1]]
res_b = ['Open', 'Open', 'Senior', 'Open']

c = [[77, 7], [33, 0], [75, 13]]
res_c = ['Open', 'Open', 'Senior']


class TestOpenOrSenior(TestCase):
    def test_input_a(self):
        self.assertEqual(res_a, openOrSenior(a))

    def test_input_b(self):
        self.assertEqual(res_b, openOrSenior(b))

    def test_input_c(self):
        self.assertEqual(res_c, openOrSenior(c))
