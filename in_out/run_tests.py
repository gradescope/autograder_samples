import unittest
import os
import subprocess32 as subprocess
from subprocess32 import PIPE
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from gradescope_utils.autograder_utils.decorators import weight

BASE_DIR = './test_data'


class TestMetaclass(type):
    """
    Metaclass that allows generating tests based on a directory.
    """
    def __new__(cls, name, bases, attrs):
        data_dir = attrs['data_dir']
        attrs[cls.test_name(data_dir)] = cls.generate_test(data_dir)
        return super(TestMetaclass, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def generate_test(cls, dir_name):
        # Return a testcase for the given directory
        command = cls.generate_command(cls, dir_name)
        n = 1                   # TODO: Allow configuring weight

        @weight(n)
        def fn(self):
            # Load command from the script
            proc = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            with open(os.path.join(BASE_DIR, dir_name, 'input')) as f:
                stdin = f.read()

            output, err = proc.communicate(stdin, 1)  # TODO: Allow configuring timeout

            # Load expected output
            with open(os.path.join(BASE_DIR, dir_name, 'output')) as f:
                expected_output = f.read()
            # TODO: Allow configuring message
            self.assertEqual(expected_output, output, msg="Output did not match expected")
        fn.__doc__ = 'Test {0}'.format(dir_name)
        return fn

    @staticmethod
    def generate_command(cls, dir_name):
        """Generates the command passed to Popen"""
        # TODO: Support args
        # TODO: allow overriding in test case
        return ["bash", "./run.sh"]

    @staticmethod
    def klass_name(dir_name):
        return 'Test{0}'.format(''.join([x.capitalize() for x in dir_name.split('_')]))

    @staticmethod
    def test_name(dir_name):
        return 'test_{0}'.format(dir_name)


def build_test_class(data_dir):
    klass = TestMetaclass(
        TestMetaclass.klass_name(data_dir),
        (unittest.TestCase,),
        {
            'data_dir': data_dir
        }
    )
    return klass


def find_data_directories():
    return filter(
        lambda x: os.path.isdir(os.path.join(BASE_DIR, x)),
        os.listdir(BASE_DIR)
    )


if __name__ == '__main__':
    suite = unittest.TestSuite()

    for name in find_data_directories():
        klass = build_test_class(name)
        suite.addTest(klass(TestMetaclass.test_name(name)))

    JSONTestRunner(visibility='visible').run(suite)
