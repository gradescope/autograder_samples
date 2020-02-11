import unittest
import random
from gradescope_utils.autograder_utils.decorators import partial_credit


class TestPartialCredit(unittest.TestCase):
    def setUp(self):
        pass

    @partial_credit(10.0)
    def test_partial(self, set_score=None):
        """Sets partial credit"""
        set_score(random.randint(0, 100) *1.0/10.0)
