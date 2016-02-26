import unittest
from autograder_utils.json_test_runner import JSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('results.json', 'w') as f:
        JSONTestRunner(stream=f, verbosity=2, buffer=True).run(suite)
