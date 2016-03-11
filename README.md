Welcome to Gradescope Autograder Documentation!

[![Documentation Status](https://readthedocs.org/projects/gradescope-autograders/badge/?version=latest)](http://gradescope-autograders.readthedocs.org/en/latest/?badge=latest)

# Overview

Gradescope provides a language-agnostic platform for running your
autograders on our infrastructure. By running in Docker containers, we
give you full flexibility in setting up whatever language, compilers,
libraries, or other dependencies you need for your programming
assignments. You provide us with a setup script and an autograder
script, along with whatever supporting code you need, and we manage
accepting student submissions, running your autograder at scale, and
distributing the results back to students and to you.

# Autograder specifications

Autograders are uploaded to Gradescope in zip format. The file must
contain at least two files in the root of the archive:

- setup.sh: a setup (Bash) script that installs all your dependencies. We're
  running on Ubuntu images, so you can use apt, or any other means of
  setting up packages.

- run_autograder: an executable script, in whatever language you want,
  that compiles and runs your autograder suite and produces the output in the correct place.

## File hierarchy

All autograder related files will be in the /autograder directory.

- /autograder/source contains the contents of your autograder zip file.
- /autograder/submission contains the student's submission, downloaded from Gradescope.
- /autograder/results/results.json is where you put the test output that is uploaded to Gradescope.


## Output format

Your autograder's output should be in the following format:

```
{ "score": 44.0, // optional, but required if not on each test case below
  "execution_time": 136, // optional, seconds
  "output": "Text relevant to the entire submission", // optional
  "tests": // Optional, but required if no top-level score
    [
        {
            "score": 2.0, // optional, but required if not on top level submission
            "max_score": 2.0, // optional
            "name": "Your name here", // optional
            "number": "1.1", // optional (will just be numbered in order of array if no number given)
            "output": "Giant multiline string that will be placed in a <pre> tag and collapsed by default", // optional
            "tags": ["tag1", "tag2", "tag3"] // optional
        },
        ...
    ]
}
```


For Java and Python, we have helper libraries that integrate with
JUnit and unittest to produce this output format easily.

# Examples

We have provided the following examples for autograders in different
languages. You can see how they are built, and use them as a starting
point for your own autograders. If you have any further questions, feel free to contact us at [help@gradescope.com](mailto:help@gradescope.com)

- [Java (JUnit)](java/)
  - [Java+maven](java-mvn/)
- [Python](python/)
