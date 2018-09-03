import unittest
import os
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner


class TestMetaclass(type):
    """
    Metaclass that allows generating tests based on a directory.
    """
    def __new__(cls, name, bases, attrs):
        data_dir = attrs['data_dir']
        attrs['test_%s' % data_dir] = cls.generate_test(data_dir)

        return super(TestMetaclass, cls).__new__(cls, name, bases, attrs)

    @classmethod
    def generate_test(cls, dir_name):
        # Return a testcase for the given directory
        def fn(self):
            self.assertEqual(dir_name, None)
        return fn

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
        {'data_dir': data_dir}
    )
    return klass


def find_data_directories():
    base_dir = './test_data'
    return filter(
        lambda x: os.path.isdir(os.path.join(base_dir, x)),
        os.listdir(base_dir)
    )


if __name__ == '__main__':
    suite = unittest.TestSuite()
    print find_data_directories()

    for name in find_data_directories():
        klass = build_test_class(name)
        suite.addTest(klass(TestMetaclass.test_name(name)))

    JSONTestRunner(visibility='visible').run(suite)
