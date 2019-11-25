# Gradescope MySQL Autograder Example

[View project source on Github](https://github.com/gradescope/autograder_samples/tree/master/mysql) - [autograder.zip](https://github.com/gradescope/autograder_samples/raw/master/mysql/autograder.zip) - [sample solution](https://github.com/gradescope/autograder_samples/raw/master/mysql/solution/queries.py)

## Project Description

This project shows an example of how one might set up a database
project on Gradescope. It installs and initializes a MySQL database
within its setup script, and then uses Python to query the database.

The actual Python connection and querying code is not intended to be
an example of how best to write such code, or how to test database
queries. It is up to you to determine how to test code that
communicates with the database. The main purpose of this example is to
show how to install, initialize, and start a service such as MySQL.

## Dependencies (for tests)

- Python 2.7+/3+
- [gradescope-utils](https://github.com/gradescope/gradescope-utils) provides decorators for setting point values for tests, and running tests with a JSON output. [See the Github repository](https://github.com/gradescope/gradescope-utils) for more on what you can do with it, or you can look at the example tests in this project for some usage examples.
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) provides a way to connect to MySQL from Python.

## Preventing Mutations to Test Data

As mentioned above, this project is not necessarily intended to
demonstrate best practices for testing database code. In particular,
this project does not show how one might prevent mutations from one
test from showing up in another test. You will probably want to
implement this for any serious testing that could involve mutations of
the test database. For example, if one test updates or deletes data in
the database, the changes should be rolled back before another test
runs. Otherwise, the validity of the tests will depend on the order in
which the tests are run, which is problematic.

# Files

## [setup.sh](https://github.com/gradescope/autograder_samples/blob/master/mysql/setup.sh)

This script installs MySQL, Python, and the pip package manager. Then
it uses pip to install our Python dependencies. It also initializes
the database state (relevant part below).

```bash
service mysql start
mysql < /autograder/source/database.sql
```

Note that while the service is started in setup.sh, this is only so
that we can initialize the database state. Because of the way Docker
works, when the autograder runs, we will still need to start the
`mysql` service manually.

## [database.sql](https://github.com/gradescope/autograder_samples/blob/master/mysql/database.sql)

This is an SQL file which initializes the database state. This is not
intended as a perfect example of SQL, but it simply demonstrates a way
to set up a database that students will access.

## [run_autograder](https://github.com/gradescope/autograder_samples/blob/master/mysql/run_autograder)

This script copies the student's submission to the target directory,
and then executes the test runner Python script. It also starts the
MySQL server, which must be done when the autograder starts, because
Docker containers do not start services automatically.

## [run_tests.py](https://github.com/gradescope/autograder_samples/blob/master/mysql/run_tests.py)

This python script loads and runs the tests using the JSONTestRunner
class from gradescope-utils. This produces the JSON formatted output
to stdout, which is then captured and uploaded by the autograder
harness.

## [framework/queries.py](https://github.com/gradescope/autograder_samples/blob/master/mysql/framework/queries.py)

This is a blank template file for the students to fill in. It provides
function signatures for methods that will query the database and
return some desired value.

## [solution/queries.py](https://github.com/gradescope/autograder_samples/blob/master/mysql/solution/queries.py)

This is a filled-in version of the above template file.

## Example Test

```
class TestSimpleQueries(unittest.TestCase):
    def setUp(self):
        self.connection = mysql.connector.connect(user='test', password='password', database='test_data')
        self.cursor = self.connection.cursor()
        self.queries = Queries(self.cursor)

    def tearDown(self):
        self.cursor.close()
        self.connection.close()

    @weight(1)
    def test_department_budget(self):
        """Get department budget by name"""
        val = self.queries.department_budget("Engineering")
        self.assertEqual(val, 1000000)
```

The title of the test case is taken from the first line of the
docstring. This is a `unittest` convention. The weight for each test is
given by the `@weight` decorator.

In this simple example, the student is filling in methods that perform
a database query given an argument, and the result is checked against
an expected value.

See all tests
[here](https://github.com/gradescope/autograder_samples/tree/master/mysql/tests)
