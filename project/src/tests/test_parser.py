import unittest
from autograder_utils.decorators import weight, tags
from framework import Calculator


class TestParser(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(1)
    @tags("parsing")
    def test_parse(self):
        """Test parsing a simple expression"""
        ast = self.calc.parse([1, '+', 1])
        self.assertEqual(ast, [1, 1, "+"])

    @weight(2)
    def test_parse2(self):
        """Test parsing with operator precedence"""
        ast = self.calc.parse([1, "+", 1, "*", 4])
        self.assertEqual(ast, [1, 1, 4, "*", "+"])

    @weight(3)
    def test_parse3(self):
        """Test parsing with parentheses"""
        ast = self.calc.parse(["(", 1, "+", 1, ")", "*", 4])
        self.assertEqual(ast, [1, 1, "+", 4, "*"])

    @weight(1)
    def test_parse4(self):
        """Test parsing with division and multiplication"""
        ast = self.calc.parse([8, "/", 4, "*", 2])
        self.assertEqual(ast, [8, 4, "/", 2, "*"])
