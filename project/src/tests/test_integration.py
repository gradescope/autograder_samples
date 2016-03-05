import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess32 as subprocess


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2)
    @tags("integration")
    def test_single_input(self):
        """Tests the full REPL"""
        calc = subprocess.Popen('python -u calculator.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        prompt = calc.stdout.read(2)  # Need to get the prompt off of stdout
        calc.stdin.write("1 + 1\n")
        calc.stdin.flush()

        output = calc.stdout.readline()
        self.assertEqual(output, "2\n")
        calc.terminate()

    @weight(2)
    @tags("integration")
    def test_quit(self):
        """Test quitting the REPL"""
        calc = subprocess.Popen('python -u calculator.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        calc.stdin.write("quit\n")
        calc.stdin.flush()

        try:
            returncode = calc.wait(1)
        except:
            pass
        if returncode is None:
            calc.terminate()
        self.assertIsNotNone(returncode)
