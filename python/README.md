# Gradescope Python Autograder Example

[View project source on Github](https://github.com/gradescope/autograder_samples/tree/master/python/src) - [autograder.zip](https://github.com/gradescope/autograder_samples/raw/master/python/src/autograder.zip) - [sample solution](https://github.com/gradescope/autograder_samples/raw/master/python/src/solution/calculator.py)

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

- Python 3.6+
- [gradescope-utils](https://github.com/gradescope/gradescope-utils) provides decorators for setting point values for tests, and running tests with a JSON output. [See the Github repository](https://github.com/gradescope/gradescope-utils) for more on what you can do with it, or you can look at the example tests in this project for some usage examples.

### Python 3

Make sure to use `pip3` and `python3` when writing your code, because in Ubuntu Python 2 is currently the default for `pip` and `python`. When installing Python 3, use the apt packages `python3` and `python3-pip`. If you need a more recent version than what is packaged by Ubuntu, you can try using a PPA or installing from source.

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

This will load tests from the `tests/` directory in your autograder source code,
[loading only files starting with `test` by default](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.discover).
`JSONTestRunner` is included in `gradescope-utils`, as described below.

# Files

## [setup.sh](https://github.com/gradescope/autograder_samples/blob/master/python/src/setup.sh)

This script installs Python and the pip package manager. Then it uses
pip to install our two external dependencies.

## [run_autograder](https://github.com/gradescope/autograder_samples/blob/master/python/src/run_autograder)

This script copies the student's submission to the target directory,
and then executes the test runner Python script.

## [run_tests.py](https://github.com/gradescope/autograder_samples/blob/master/python/src/run_tests.py)

This python script loads and runs the tests using the JSONTestRunner
class from gradescope-utils. This produces the JSON formatted output
to stdout, which is then captured and uploaded by the autograder
harness.

## [framework.py](https://github.com/gradescope/autograder_samples/blob/master/python/src/framework.py)

This is a blank template file for the students to fill in. Note that
their solution must be called calculator.py for the autograder to work
correctly.
