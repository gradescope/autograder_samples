# autograder_utils

This package provides some helper classes which assist in developing autograders
for the Gradescope autograder platform. These utilities work together to make it
easy to use Python's built in `unittest` module for creating autograders that
work on Gradescope.

## decorators

Two decorators are provided for annotating test cases.

### @weight

The `@weight` decorator allows setting the point value of a test case. This
information is used by the JSONTestRunner in producing its output. This is
required for any tests which award points.

Example:
```
@weight(5.0)
def test_functionality():
    ...
```

### @tags

The `@tags` decorator allows setting tags on a test case. This is optional, but
may be used in the future to enable analytics on the concepts being tested in
programming assignments.

Example:
```
@tags("conditionals", "recursion")
def test_search():
    ...
```

## unittest utilities

### JSONTestRunner

This utility class is a custom unittest test runner which produces JSON output
in the format that Gradescope's infrastructure expects. It works with test cases
annotated with the `@weight` annotation to determine the point value of each
test case.

Example:
```
suite = unittest.defaultTestLoader.discover('tests')
with open('results.json', 'w') as f:
    JSONTestRunner(stream=f, verbosity=2, buffer=True).run(suite)
```

### JSONTestResult

This class is used by JSONTestRunner to format output in JSON.

Example output:

```
{
    "output": "Printing inside a test case\n",
    "score": 3,
    "max_score": 3,
    "name": "Test parsing a simple expression",
    "tags": [
        "parsing",
        "lexing"
    ]
}
```
