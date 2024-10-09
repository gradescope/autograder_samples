import doctest
import unittest
from gradescope_utils.autograder_utils.decorators import partial_credit


# TODO: change this to fit your case.
import filepath_submitted as student_module


class TestDoctests(unittest.TestCase):
    def setUp(self):
        pass

    @partial_credit(10.0)
    def test_doctests(self, set_score=None):
        """Evaluate your doc-tests"""
        tests_failed, tests_run = doctest.testmod(student_module,
                                                  optionflags=doctest.ELLIPSIS)
        if tests_run == 0:
            print("You need to write doc-tests")
            return set_score(0)
        
        set_score(10 * (tests_run - tests_failed) / tests_run)
