import unittest
from gradescope_utils.autograder_utils.decorators import weight
from calculator import Calculator


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
        """Test evaluating 2-1"""
        rpn = [2, 1, "-"]
        val = self.calc.eval(rpn)
        self.assertEqual(val, 1)

    @weight(1)
    def test_eval3(self):
        """Test evaluating (1+1)*4"""
        rpn = [1, 1, "+", 4, "*"]
        val = self.calc.eval(rpn)
        self.assertEqual(val, 8)

    @weight(1)
    def test_eval4(self):
        """Test evaluating 8/4"""
        rpn = [8, 4, "/"]
        val = self.calc.eval(rpn)
        self.assertEqual(val, 2)
