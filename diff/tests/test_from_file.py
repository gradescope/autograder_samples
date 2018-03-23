import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess32 as subprocess


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    def test_from_file(self):
        """10th Fibonacci number"""
        fib = subprocess.Popen(["./fib", "10"], stdout=subprocess.PIPE)
        output = fib.stdout.read().strip()
        with open("reference/10", "r") as outputFile:
            referenceOutput = outputFile.read()

        self.assertEqual(output, referenceOutput)
        fib.terminate()
