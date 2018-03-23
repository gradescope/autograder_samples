# Overview

[View project source on GitHub](https://github.com/gradescope/autograder_samples/tree/master/diff)

This is an example of using Python and the gradescope-utils library to
implement diff-style autograding of a C assignment. The idea is that
you can compile the student's code, and then execute it in a
subprocess using Python. Then you can communicate with the subprocess
by providing arguments via the command line, or via standard input,
and read standard output to see what the program produced. Finally,
you check the output against a reference answer and decide whether the
test case passed or failed.

The basic structure of this autograder example is the same as the
regular Python example, so you may want to familiarize yourself with
that one first.

## The program

The C program in question ([`fib.c`](https://github.com/gradescope/autograder_samples/blob/master/diff/fib.c)) computes the nth Fibonacci number
(1-indexed), as specified as the first command line argument
(i.e. `argv[1]`). This is just a simple example to demonstrate how you
might structure such an autograder.

## Compiling the C code

For this simple example of a one-file C program, it can be compiled by
running `make fib`. In general, you will need to compile the code
within `run_autograder` before starting the Python script. This can be
as complicated as you need it to be - you can actually write a
Makefile or use whatever other build system you need to use.

## Providing input to the program

This example uses command line arguments because that was the easiest thing
to do, but you can also write to the subprocess's standard
input. You can see the [Python integration test](https://github.com/gradescope/autograder_samples/blob/master/python/src/tests/test_integration.py)
for an example of how to do that.

## Comparing to the reference answers

Once you've read the program's output, you should compare them to your
reference answers. You can either put the values directly in the unit
tests, or you can load them from a file. Either way, you will want to
check the student's results by asserting something about their output
in relation to the reference.

Reference in unit test:

```python
def test_fib1(self):
    """1st Fibonacci Number"""
    fib = subprocess.Popen(["./fib", "1"], stdout=subprocess.PIPE)
    output = fib.stdout.read().strip()
    referenceOutput = "1"
    self.assertEqual(output, referenceOutput)
    fib.terminate()
```

Loading from a file:

```python
def test_from_file(self):
    """10th Fibonacci number"""
    fib = subprocess.Popen(["./fib", "10"], stdout=subprocess.PIPE)
    output = fib.stdout.read().strip()
    with open("reference/10", "r") as outputFile:
        referenceOutput = outputFile.read()

    self.assertEqual(output, referenceOutput)
    fib.terminate()
```
