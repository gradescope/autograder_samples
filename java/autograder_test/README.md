# Gradescope Java Autograder Example

This example shows how to set up an autograder on Gradescope for a
Java project. It uses JUnit, JDK8, Maven, and Josh Hug's jh61b library
for producing output in JSON format.

## Explanation of Dependencies

- JUnit: Popular Java unit testing framework
- jh61b: Among other things, this provides annotations for JUnit tests that allows setting point values and names, and a test listener that produces output in JSON format
- JDK8: jh61b uses String.join() which is added in JDK8. If you need versions <8, you just need to replace this part of the code
- Maven: Build tool. Provides dependency resolution (only needed for JUnit and exec plugin in this project) and a way to compile and execute code (using exec plugin)

## [setup.sh](setup.sh)

Sets up JDK 8 and maven. There's a workaround for a ca-certificates
issue to make sure you can install things from Maven.

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

mvn compile is a built in maven goal to compile the project. -q makes
it quiet.

mvn exec:java is a goal from the exec plugin for maven. It lets you
specify a main class to execute (see pom.xml). This lets you avoid
having to figure out the proper java command to run and classpath
arguments and such.

## [pom.xml](pom.xml)

This is a maven project file. Briefly, it describes the project, its
dependencies, Java compiler version, and main class.

This file and the project structure were generated using the command

`mvn archetype:generate -DgroupId=com.gradescope.autograder_test -DartifactId=autograder_test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false`
