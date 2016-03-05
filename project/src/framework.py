# Place your imports here


class CalculatorException(Exception):
    """A class to throw if you come across incorrect syntax or other issues"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


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

    def eval(self, string):
        """Evaluates an infix arithmetic expression"""
        # TODO: Implement me
        pass

    def loop(self):
        """Runs the read-eval-print loop

        Read a line of input, evaluate it, and print it.

        Repeat the above until the user types 'quit'."""
        # TODO: Implement me
        pass

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
