from unittest import TestSuite
from test_parser import TestParser
from test_evaluator import TestEvaluator
test_cases = (TestParser, TestEvaluator)


def load_tests(loader, tests, pattern):
    suite = TestSuite()
    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite
