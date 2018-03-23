# Overview

This is an example of using Python and the gradescope-utils library to
implement diff-style autograding of a C assignment. The idea is that
you can compile the student's code, and then execute it in a
subprocess using Python. Then you can communicate with the subprocess
by providing arguments via the command line, or via standard input,
and read standard output to see what the program produced. Finally,
you check the output against a reference answer and decide whether the
test case passed or failed.

## Compiling the C code

I chose a very simple example of a one-file C program, which can just
be compiled by running `make fib`. You will need to compile the code
within `run_autograder`. This can be as complicated as you need it to
be, or you can actually write a Makefile or use whatever other build
system you need to use.

## Providing input to the program

I just used command line arguments because that was the easiest thing
to do, but you can also use write to the subprocess's standard
input. You can see the [Python integration test](https://github.com/gradescope/autograder_samples/blob/master/python/src/tests/test_integration.py)
for an example of that.

## Comparing to the reference answers

I put the reference answers in the Python unit tests, but you might
consider putting them in files, and then reading the files from the
filesystem and checking them that way.
