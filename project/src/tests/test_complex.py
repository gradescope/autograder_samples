import unittest
from gradescope_utils.autograder_utils.decorators import weight
from calculator import Calculator


class TestComplex(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(2)
    def test_eval_parens(self):
        """Test evaluating (1 + 1) * 4"""
        val = self.calc.eval("(1 + 1) * 4")
        self.assertEqual(val, 8)

    @weight(2)
    def test_eval_precedence(self):
        """Test evaluating 1 + 1 * 8"""
        val = self.calc.eval("1 + 1 * 8")
        self.assertEqual(val, 9)

    @weight(2)
    def test_eval_mul_div(self):
        "Test evaluating 8 / 4 * 2"
        val = self.calc.eval("8 / 4 * 2")
        self.assertEqual(val, 4)

    @weight(2)
    def test_eval_negative_number(self):
        "Test evaluating -2 + 6"
        val = self.calc.eval("-2 + 6")
        self.assertEqual(val, 4)
