import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from calculator import Calculator


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(2)
    @visibility('after_due_date')
    @number("2.1")
    def test_eval_parens(self):
        """Evaluate (1 + 1) * 4"""
        val = self.calc.eval("(1 + 1) * 4")
        self.assertEqual(val, 8)

    @weight(2)
    @visibility('after_due_date')
    @number("2.2")
    def test_eval_precedence(self):
        """Evaluate 1 + 1 * 8"""
        val = self.calc.eval("1 + 1 * 8")
        self.assertEqual(val, 9)

    @weight(2)
    @number("2.3")
    def test_eval_mul_div(self):
        """Evaluate 8 / 4 * 2"""
        val = self.calc.eval("8 / 4 * 2")
        self.assertEqual(val, 4)

    @weight(2)
    @number("2.4")
    def test_eval_negative_number(self):
        """Evaluate -2 + 6"""
        val = self.calc.eval("-2 + 6")
        self.assertEqual(val, 4)
