import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from calculator import Calculator, CalculatorException


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(2)
    @visibility('after_published')
    def test_eval_power(self):
        """Evaluating 2 ** 8 should raise an exception"""
        with self.assertRaises(CalculatorException):
            self.calc.eval("2 ** 8")
