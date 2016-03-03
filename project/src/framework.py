# Place your imports here


class Calculator(object):
    """Infix calculator REPL

    Parses and evaluates infix arithmetic with the 4 basic operators
    and parentheses. Must obey order of operations.
    """

    def is_digit(self, token):
        # TODO: You may find these functions useful to implement
        pass

    def is_operator(self, token):
        pass

    def is_paren(self, token):
        pass

    def is_operand(self, token):
        pass

    def read(self):
        """
        Read input from stdin
        """
        return raw_input('> ')

    def lexer(self, string):
        """Break an input string into tokens"""
        # TODO Implement me
        pass

    def parse(self, tokens):
        """Turns an infix arithmetic string into an RPN representation
        """
        # TODO Implement me
        pass

    def eval(self, rpn):
        """Evaluates an RPN expression in list form
        """
        # TODO Implement me
        pass

    def loop(self):
        line = self.read()
        while line != "quit":
            tokens = self.lexer(line)
            ast = self.parse(tokens)
            value = self.eval(ast)
            print value
            # Read next line of input
            line = self.read()

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
