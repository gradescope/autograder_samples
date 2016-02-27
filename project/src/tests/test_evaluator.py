import unittest
from autograder_utils.decorators import weight
from framework import Calculator


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(2)
    def test_eval(self):
        """Test evaluating 1+1"""
        rpn = [1, 1, "+"]
        val = self.calc.eval(rpn)
        self.assertEqual(val, 2)

    @weight(1)
    def test_eval2(self):
        """Test evaluating (1+1)*4"""
        rpn = [1, 1, "+", 4, "*"]
        val = self.calc.eval(rpn)
        self.assertEqual(val, 8)
