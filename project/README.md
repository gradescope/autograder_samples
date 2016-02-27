% Infix Calculator REPL

# Introduction

This assignment will guide you in building an infix calculator
REPL. The goal of this project is to teach you the basics of parsing
and evaluating a simple language.

# Tasks

## Tokenization

Before we can begin parsing the input, we must break it up into tokens

## Parsing - The Shunting-yard Algorithm


* While there are tokens to be read:
    * Read a token.
    * If the token is a number, then add it to the output queue.

    * If the token is an operator, $o_1$, then

        * while there is an operator token $o_2$, at the top of the operator stack and either
        $o_1$ is left-associative and its precedence is less than or equal to that of $o_2$, or
        $o_1$ is right associative, and has precedence less than that of $o_2$,

        * pop $o_2$ off the operator stack, onto the output queue;

        * at the end of iteration push $o_1$ onto the operator stack.

    * If the token is a left parenthesis (i.e. "("), then push it onto the stack.
    * If the token is a right parenthesis (i.e. ")"):
        * Until the token at the top of the stack is a left parenthesis, pop operators off the stack onto the output queue.
        * Pop the left parenthesis from the stack, but not onto the output queue.
        * If the stack runs out without finding a left parenthesis, then there are mismatched parentheses.

* When there are no more tokens to read:
    * While there are still operator tokens in the stack:
        * If the operator token on the top of the stack is a parenthesis, then there are mismatched parentheses.
        * Pop the operator onto the output queue.

* Exit.

## Evaluation

# Framework

# Testing
