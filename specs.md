# Autograder Specifications

Autograders are uploaded to Gradescope in zip format. The file must
contain at least two files in the root of the archive:

- **setup.sh**: a setup (Bash) script that installs all your dependencies. We're
  running on Ubuntu images, so you can use apt, or any other means of
  setting up packages.

- **run_autograder**: an executable script, in any language (with
  appropriate `#!` line), that compiles and runs your autograder suite
  and produces the output in the correct place.

## File hierarchy

All autograder related files will be in the /autograder directory.

- **/autograder/source** contains the contents of your autograder zip file.
- **/autograder/submission** contains the student's submission, downloaded from Gradescope.
- **/autograder/results/results.json** is where you put the test output that is uploaded to Gradescope.
- **/autograder/results/stdout** captures the output of run_autograder, for displaying back to the instructor for debugging purposes. Any output you wish to show to students must be explicitly put in the JSON "output" field.

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
        // and more test cases...
    ]
}
```


For Java and Python, we have helper libraries that integrate with
JUnit and unittest to produce this output format easily.
