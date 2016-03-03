import re


class Calculator(object):
    """
    """
    # TODO Fillme
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
        """
        Read input from stdin
        """
        return raw_input('> ')

    def lexer(self, string):
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
            print "Unknown character", string[i]
            i = i + 1
        return tokens

    def parse(self, tokens):
        """Turns an infix arithmetic string into an RPN representation
        """
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
                        val = op1 - op2
                    elif token == '*':
                        val = op1 * op2
                    elif token == '/':
                        val = op1 / op2
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
