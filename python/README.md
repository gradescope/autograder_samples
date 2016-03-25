# Gradescope Python Autograder Example

[View project source on Github](https://github.com/gradescope/autograder_samples/tree/master/python/src)

## Project Description

In this assignment, students will build an infix calculator REPL. The
goal of this project is to teach the basics of parsing and evaluating
a simple language.

**Requirements**

* Build an infix calculator read-eval-print loop
* The calculator should handle the 4 basic operations, +, -, *, /, with operator precedence
* In addition, it should handle parentheses and negative numbers
* If the user types 'quit', exit the program
* If there are syntax errors in the user input, raise CalculatorException

## Dependencies (for tests)

- Python 2.7+ (should work with Python 3 as well if students use it; the tests don't use anything Python2 specific)
- Python's unittest module is built in
- gradescope-utils provides annotations for setting point values for tests, and running tests with a JSON output.
- subprocess32 is a convenient backport of Python 3.2's subprocess module. Used in one of the tests to communicate with an instance of the REPL to verify that it responds to input correctly.

## Example Test

```
class TestSimpleArithmetic(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @weight(1)
    def test_eval_add(self):
        """Evaluate 1 + 1"""
        val = self.calc.eval("1 + 1")
        self.assertEqual(val, 2)
```

The title of the test case is taken from the first line of the
docstring. This is a `unittest` convention. The weight for each test is
given by the `@weight` decorator.

See all tests
[here](https://github.com/gradescope/autograder_samples/tree/master/python/src/tests)

## Running Tests

```
suite = unittest.defaultTestLoader.discover('tests')
JSONTestRunner().run(suite)

```

# Files

## [setup.sh](src/setup.sh)

This script installs Python and the pip package manager. Then it uses
pip two install our two external dependencies.

## [run_autograder](src/run_autograder)

This script copies the student's submission to the target directory,
and then executes the test runner Python script.

## [run_tests.py](src/run_tests.py)

This python script loads and runs the tests using the JSONTestRunner
class from gradescope-utils. This produces the JSON formatted output
to stdout, which is then captured and uploaded by the autograder
harness.

## [framework.py](src/framework.py)

This is a blank template file for the students to fill in. Note that
their solution must be called calculator.py for the autograder to work
correctly.
