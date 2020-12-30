import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
import subprocess


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    @weight(2)
    @tags("integration")
    def test_single_input(self):
        """Evaluate 1 + 1 in the REPL"""
        calc = subprocess.Popen('python3 -u calculator.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        output, err = calc.communicate("1 + 1\n", 1)
        self.assertTrue(output.startswith(">"))    # Check for presence of prompt
        answer = output[1:].split()[0]             # Separate prompt from answer
        self.assertEqual(answer.strip(), "2")
        calc.terminate()

    @weight(2)
    @tags("integration")
    def test_quit(self):
        """Quit the REPL"""
        calc = subprocess.Popen('python3 -u calculator.py'.split(),
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                encoding='utf8')
        calc.communicate("quit\n", 1)

        returncode = calc.returncode
        if returncode is None:
            calc.terminate()
        self.assertIsNotNone(returncode)
        self.assertEqual(returncode, 0)
