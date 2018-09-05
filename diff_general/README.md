# Overview

[View project source on GitHub](https://github.com/gradescope/autograder_samples/tree/master/diff_general)

This is an example of using Python and the gradescope-utils library to
implement diff-style autograding of a C assignment. The idea is that
you can compile the student's code, and then execute it in a
subprocess using Python. Then you can communicate with the subprocess
by providing arguments via the command line, or via standard input,
and read standard output to see what the program produced. The
student's output is checked against a reference answer to decide
whether the test case passed or failed.

This type of testing helps with testing assignments that are not
easily amenable to unit testing, such as assignments where students
don't necessarily write specific functions.

## Building and executing code

- **compile.sh**: This script should do whatever is necessary to
  compile the student's code. If nothing needs to be compiled, you can
  use this file to copy the student's files to the right directory.
- **run.sh**: This script should run the student's program. This can
  be overridden for a given test case.

## Adding test cases

This example is driven entirely by the files that are in the `test_data`
directory, i.e. to add test cases you only have to add directories to the
`test_data` directory. Each test case should have the following files:

- **input**: This file will be fed to the program over standard input.
- **output**: This file will serve as the reference output for the
  test, and must be matched for the test to pass.
- **settings.yml**: This file holds various settings, such as the
  weight assigned to a test case.
- **err**: Optionally, this file can be used to compare any output
  that is expected to be printed to standard error.
- **run.sh**: Optionally, you can override the command used to execute
  this test case. This can be used to provide different command line
  arguments.

## The example program

The C program in question ([`fib.c`](https://github.com/gradescope/autograder_samples/blob/master/diff_general/fib.c)) computes the nth Fibonacci number
(1-indexed), as specified as the first command line argument
(i.e. `argv[1]`). This is just a simple example to demonstrate how you
might structure such an autograder.

## Providing input to the program

You can provide command line arguments in run.sh, or you can send
input to standard input using the `input` file.
