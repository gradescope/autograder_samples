import unittest
import os
import os.path
import subprocess32 as subprocess
from subprocess32 import PIPE
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
        """ Returns a testcase for the given directory """
        command = cls.generate_command(dir_name)
        n = 1                   # TODO: Allow configuring weight

        def load_test_file(path):
            full_path = os.path.join(BASE_DIR, dir_name, path)
            if os.path.isfile(full_path):
                with open(full_path) as f:
                    return f.read()
            return None

        @weight(n)
        def fn(self):
            proc = subprocess.Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            stdin = load_test_file('input')

            output, err = proc.communicate(stdin, 1)  # TODO: Allow configuring timeout

            expected_output = load_test_file('output')
            expected_err = load_test_file('err')

            # TODO: Allow configuring message
            self.assertEqual(expected_output, output, msg="Output did not match expected")
            if expected_err is not None:
                self.assertEqual(expected_err, err, msg="Error output did not match expected")
        fn.__doc__ = 'Test {0}'.format(dir_name)
        return fn

    @staticmethod
    def generate_command(dir_name):
        """Generates the command passed to Popen"""
        test_specific_script = os.path.join(BASE_DIR, dir_name, 'run.sh')
        if os.path.isfile(test_specific_script):
            return ["bash", test_specific_script]
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
