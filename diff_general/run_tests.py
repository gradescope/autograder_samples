import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from test_generator import find_data_directories, build_test_class, TestMetaclass

if __name__ == '__main__':
    suite = unittest.TestSuite()

    for name in find_data_directories():
        klass = build_test_class(name)
        suite.addTest(klass(TestMetaclass.test_name(name)))

    with open('/autograder/results/results.json', 'w') as f:
        JSONTestRunner(visibility='visible', stream=f).run(suite)
