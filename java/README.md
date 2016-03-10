# Gradescope Java Autograder Example

This example shows how to set up an autograder on Gradescope for a
Java project. It uses JUnit, JDK8, and Josh Hug's jh61b library for
producing output in JSON format.

## Explanation of Dependencies

- JUnit: Popular Java unit testing framework
- jh61b: Among other things, this provides annotations for JUnit tests that allows setting point values and names, and a test listener that produces output in JSON format
- JDK8: jh61b uses String.join() which is added in JDK8. If you need versions <8, you just need to replace this part of the code

## [setup.sh](setup.sh)

Sets up OpenJDK 8.

Note: Installing JDK8 takes a few minutes, so building the image takes
a while. We may want to provide base images with JDK installed to
speed that up, though it's really only a few minutes once so it might
not matter to you.

## [run_autograder](run_autograder)

Copies the student's code to the autograder directory, compiles, and
executes it.

One thing to be aware of for Java projects is that you need to copy
the student's work to the right place depending on the
package. Depending on how you set up the project, students may submit
files in the root of their submission or within nested directories for
the package they used. Either is fine, you just need to sure that when
you're copying the files around you put them in the right place. Your
autograder code should know what package to import from, so make sure
that you know ahead of time what the student's package is (i.e. tell
them what to do or set up a template that has it filled in).

This script calls compile.sh and run.sh to compile and run code.

### [compile.sh](compile.sh)

This script finds all source files under the *src* directory and
compiles them. It adds the junit and hamcrest jars in the lib
directory to the classpath (hamcrest is a dependency of JUnit). It
produces output in the *classes* directory.

### [run.sh](run.sh)

This script just runs the IntListTest class. It adds the compiled
classes and bundled libraries to the classpath.

## [IntListTest.java](src/main/java/com/gradescope/autograder_test/IntListTest.java)

This is the actual Test class. It imports the necessary parts of
jh61b, JUnit, and the student's code. Then, it runs a set of basic
tests on the student's code.

## [IntList.java](src/main/java/com/gradescope/autograder_test/IntList.java)

This is a "reference implementation" of the IntList class. It's just a
linked list for ints. One possible approach to writing tests is to
have your reference implementation as part of your autograder, and
compare the student's return values to the reference
implementation. Also, if you need to rely on certain functions in the
student's code working for some tests, you should use your reference
implementation to set up the test data structures and then call the
student's code.

You can also submit this code to the autograder to see it work. In the
current version of the autograder it relies on the student's code
being in the same package as the autograder, for simplicity, but this
could be changed.
