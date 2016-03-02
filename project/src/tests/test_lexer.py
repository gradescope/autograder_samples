import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from calculator import Calculator


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(1)
    @tags("lexing")
    def test_lex1(self):
        """Test lexing a simple expression"""
        tokens = self.calc.lexer("1 + 1")
        self.assertEqual(tokens, [1, "+", 1])

    @weight(1)
    @tags("lexing")
    def test_lex2(self):
        """Test lexing a simple expression without whitespace"""
        tokens = self.calc.lexer("1+1")
        self.assertEqual(tokens, [1, "+", 1])

    @weight(2)
    @tags("lexing")
    def test_lex3(self):
        """Test lexing an expression with parentheses"""
        tokens = self.calc.lexer("2*(1+1)")
        self.assertEqual(tokens, [2, "*", "(", 1, "+", 1, ")"])
