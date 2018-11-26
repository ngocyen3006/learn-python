from unittest import TestCase
from firstEquation import Equation


class TestLinearEquation(TestCase):
    def test_is_contrary_equation(self):
        self.assertEqual("Contrary equation", Equation(0, 10).solve())

    def test_is_identity_equation(self):
        self.assertEqual("Identity equation", Equation(0, 0).solve())

    def test_the_equation_has_one_solution(self):
        self.assertEqual(2.0, Equation(5, -10).solve())
        self.assertEqual(-2.25, Equation(4, 9).solve())
