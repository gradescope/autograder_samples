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

    def lex(self, string):
        return string.split()

    def eval(self, string):
        """Evaluates an infix arithmetic expression"""
        # TODO: Implement me
        tokens = self.lex(string)
        op1 = int(tokens.pop(0))
        while len(tokens) > 0:
            operator = tokens.pop(0)
            op2 = int(tokens.pop(0))
            if operator == '+':
                op1 = op1 + op2
            elif operator == '-':
                op1 = op1 - op2
            elif operator == '*':
                op1 = op1 * op2
            elif operator == '/':
                op1 = op1 / op2
            else:
                raise CalculatorException("Unknown operator %s" % operator)
        return op1

    def loop(self):
        """Runs the read-eval-print loop

        Read a line of input, evaluate it, and print it.

        Repeat the above until the user types 'quit'."""
        # TODO: Implement me
        line = self.read()
        while line != "quit":
            value = self.eval(line)
            print value
            line = self.read()

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
