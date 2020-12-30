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

    def read(self):
        """Read input from stdin"""
        return input('> ')

    def lex(self, string):
        """Break the string up into tokens"""
        return string.split()

    def eval(self, string):
        """Evaluates an infix arithmetic expression"""
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
        line = self.read()
        while line != "quit":
            value = self.eval(line)
            print(value)
            line = self.read()

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
