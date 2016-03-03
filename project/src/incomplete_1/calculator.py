import re


class Calculator(object):
    """Infix calculator REPL

    Parses and evaluates infix arithmetic with the 4 basic operators
    and parentheses. Must obey order of operations.
    """
    DIGIT = re.compile('\-?\d+')
    WHITESPACE = re.compile('\s+')
    OPERATOR = re.compile('[\+\-\*\/]')
    PAREN = re.compile('[\(\)]')

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
        """
        Read input from stdin
        """
        return raw_input('> ')

    def lexer(self, string):
        """Break an input string into tokens"""
        t1 = string.split()
        tokens = []
        for t in t1:
            try:
                x = int(t)
                tokens.append(x)
            except ValueError:
                tokens.append(t)
        return tokens

    def parse(self, tokens):
        """Turns an infix arithmetic string into an RPN representation
        """
        pass

    def eval(self, rpn):
        """Evaluates an RPN expression in list form
        """
        stack = []
        while len(rpn) > 0:
            token = rpn.pop(0)
            if type(token) == int:
                stack.append(token)
            else:  # token is an operator
                if len(stack) < 2:
                    raise Exception("Not enough inputs for operator", token)
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
            raise Exception("Too many input values")

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
