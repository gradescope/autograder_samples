import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess32 as subprocess


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass

    @weight(1)
    def test_no_args(self):
        """Invalid Input (no argument)"""
        fib = subprocess.Popen(["./fib"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = fib.stdout.read().strip()
        self.assertEqual(output, "")
        err = fib.stderr.read().strip()
        referenceOutput = "Error: Insufficient arguments."
        self.assertEqual(err, referenceOutput)
        fib.terminate()

    @weight(1)
    def test_fib0(self):
        """Invalid Input (0)"""
        fib = subprocess.Popen(["./fib", "0"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = fib.stdout.read().strip()
        self.assertEqual(output, "")
        err = fib.stderr.read().strip()
        referenceOutput = "Error: number must be greater than 0."
        self.assertEqual(err, referenceOutput)
        fib.terminate()

    @weight(1)
    def test_fib1(self):
        """1st Fibonacci Number"""
        fib = subprocess.Popen(["./fib", "1"], stdout=subprocess.PIPE)
        output = fib.stdout.read().strip()
        referenceOutput = "1"
        self.assertEqual(output, referenceOutput)
        fib.terminate()

    @weight(1)
    def test_fib2(self):
        """2nd Fibonacci Number"""
        fib = subprocess.Popen(["./fib", "2"], stdout=subprocess.PIPE)
        output = fib.stdout.read().strip()
        referenceOutput = "1"
        self.assertEqual(output, referenceOutput)
        fib.terminate()

    @weight(1)
    def test_fib3(self):
        """3rd Fibonacci Number"""
        fib = subprocess.Popen(["./fib", "3"], stdout=subprocess.PIPE)
        output = fib.stdout.read().strip()
        referenceOutput = "2"
        self.assertEqual(output, referenceOutput)
        fib.terminate()

    @weight(1)
    def test_fib4(self):
        """4th Fibonacci number"""
        fib = subprocess.Popen(["./fib", "4"], stdout=subprocess.PIPE)
        output = fib.stdout.read().strip()
        referenceOutput = "3"
        self.assertEqual(output, referenceOutput)
        fib.terminate()
