import unittest
import tests
from json_test_runner import JSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromModule(tests)
    JSONTestRunner(verbosity=2, buffer=True).run(suite)
