import unittest
from autograder_utils.decorators import weight


class TestEvaluator(unittest.TestCase):
    @weight(3)
    def test_eval(self):
        self.assertTrue(True)

    @weight(1)
    def test_eval2(self):
        self.assertTrue(True)
