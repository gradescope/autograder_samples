# Gradescope C# Autograder Example

[View project source on Github](https://github.com/gradescope/autograder_samples/tree/master/c#/src) - [autograder.zip](https://github.com/gradescope/autograder_samples/raw/master/c#/src/autograder.zip) - [sample solution](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/solution/HelloWorld.cs)

## Project Description

This project is a simple example of how to build a C# autograder.



## Dependencies (for tests)

- Python 3+
- NUnit

## Example Test

```
[TestFixture]
public class HelloWorldTest
{
    [Test, Property("Weight", 1.0), Property("Visibility", "visible")]
    public void HelloTest()
    {
        Assert.AreEqual(HelloWorld.Hello(), "Hello");
    }

    [Test, Property("Weight", 2.0), Property("Visibility", "hidden"), Property("Name", "Bye")]
    public void MyTest2()
    {
        Assert.AreEqual(HelloWorld.Bye(), "Bye");
    }
}
```

## Running Tests

```
mcs -target:library -pkg:nunit -out:test.dll test.cs HelloWorld.cs
nunit-console test.dll
```

# Files

## [setup.sh](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/setup.sh)

This script installs NUnit and the Mono development tools.

## [run_autograder](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/run_autograder)

This script copies the student's submission to the target directory,
compiles the required files (the test case and the student's submission),
executes the test suite, and then converts the XML test results to Gradescope's
JSON format.

## [nunit_to_gs.py](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/nunit_to_gs.py)

This python script loads the test results from TestResults.xml
and converts them into Gradescope's JSON format. This script is what
reads the property tags that you supplied in the test case, as shown above,
and turns those into the appropriate Gradescope metadata.

## [Framework.cs](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/Framework.cs)

This is a blank template file for the students to fill in. Note that
their solution must be called HelloWorld.cs for the autograder to work
correctly.

## [autograder.zip](https://github.com/gradescope/autograder_samples/blob/master/c%23/src/autograder.zip)

This is a zipped up autograder that can be directly uploaded to Gradescope.
You can then try out the correct and/or incorrect solutions we provide to see how
the autograder works.
