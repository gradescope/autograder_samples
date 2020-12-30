import re


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
    DIGIT = re.compile('\-?\d+')
    WHITESPACE = re.compile('\s+')
    OPERATOR = re.compile('[\+\-\*\/]')
    PAREN = re.compile('[\(\)]')
    TOKEN_CLASSES = [DIGIT, WHITESPACE, OPERATOR, PAREN]
    PRECEDENCES = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 0,  # For precedence matters, parens don't count
        ')': 0
    }

    def is_digit(self, token):
        return self.DIGIT.match(token)

    def is_operator(self, token):
        return self.OPERATOR.match(token)

    def is_paren(self, token):
        return self.PAREN.match(token)

    def is_operand(self, token):
        return self.is_digit(token) or self.is_paren(token)

    def read(self):
        """Read input from stdin"""
        return input('> ')

    def lex(self, string):
        """Break an input string into tokens"""
        tokens = []
        i = 0
        while i < len(string):
            match = self.DIGIT.match(string, i)
            if match:
                tokens.append(int(match.group()))
                i = match.end()
                continue
            match = self.WHITESPACE.match(string, i)
            if match:
                i = match.end()
                continue
            match = self.OPERATOR.match(string, i)
            if match:
                tokens.append(match.group())
                i = match.end()
                continue
            match = self.PAREN.match(string, i)
            if match:
                tokens.append(match.group())
                i = match.end()
                continue
            raise CalculatorException("Unknown character".format(string[i]))
            i = i + 1
        return tokens

    def parse(self, tokens):
        """Turns an infix arithmetic string into an RPN representation.

        Uses the Shunting yard algorithm. This is used to resolve operator
        precedence and handle parentheses."""
        output = []
        operator_stack = []
        while len(tokens) > 0:
            token = tokens.pop(0)

            if type(token) == int:
                output.append(token)
            elif self.is_operator(token):
                precedence = self.PRECEDENCES[token]
                while len(operator_stack) > 0 and \
                        precedence <= self.PRECEDENCES[operator_stack[-1]]:
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Pop the left paren
        while len(operator_stack) > 0:
            output.append(operator_stack.pop())
        return output

    def eval_rpn(self, rpn):
        """Evaluates an RPN expression in list form"""
        stack = []
        while len(rpn) > 0:
            token = rpn.pop(0)
            if type(token) == int:
                stack.append(token)
            else:  # token is an operator
                if len(stack) < 2:
                    raise CalculatorException("Not enough inputs for operator {0}".format(token))
                else:
                    op1 = stack.pop()
                    op2 = stack.pop()
                    if token == '+':
                        val = op1 + op2
                    elif token == '-':
                        val = op2 - op1
                    elif token == '*':
                        val = op1 * op2
                    elif token == '/':
                        val = op2 / op1
                    stack.append(val)
        if len(stack) == 1:
            return stack[0]
        else:
            raise CalculatorException("Too many input values")

    def eval(self, string):
        """Evaluates an infix arithmetic expression"""
        tokens = self.lex(string)
        ast = self.parse(tokens)
        value = self.eval_rpn(ast)
        return value

    def loop(self):
        """Runs the read-eval-print loop

        Read a line of input, evaluate it, and print it.

        Repeat the above until the user types 'quit'."""
        line = self.read()
        while line != "quit":
            value = self.eval(line)
            print(value)
            # Read next line of input
            line = self.read()

if __name__ == '__main__':
    calc = Calculator()
    calc.loop()
