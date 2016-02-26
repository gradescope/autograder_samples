import unittest
from util import weight, tags


class TestParser(unittest.TestCase):
    @weight(3)
    @tags("parsing", "lexing")
    def test_parse(self):
        """Test parsing a simple expression"""
        print "Printing inside a test case"
        self.assertTrue(True)

    @weight(1)
    def test_parse2(self):
        self.assertTrue(True)
