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

All autograder related files will be in the /autograder directory. This directory structure is set up when the autograder Docker image is built.

Files you provide:

- **/autograder/source** contains the extracted contents of your autograder zip file.
- **/autograder/run_autograder** is where your autograder script gets copied to during the Docker image build process.
- **/autograder/results/results.json** is where you put the test output that is uploaded to Gradescope. This must be produced as a result of executing `run_autograder`.

Gradescope's autograder harness will create the following files:

- **/autograder/submission** contains the student's submission, downloaded from Gradescope.
- **/autograder/results/stdout** captures the output of `run_autograder`, for displaying back to the instructor for debugging purposes. Any output you wish to show to students must be explicitly put in the JSON "output" field.

## Output format

Your autograder's output should be in the file results.json, in the following format:

```
{ "score": 44.0, // optional, but required if not on each test case below
  "execution_time": 136, // optional, seconds
  "output": "Text relevant to the entire submission", // optional
  "visibility": "after_due_date" // Optional visibility setting
  "tests": // Optional, but required if no top-level score
    [
        {
            "score": 2.0, // optional, but required if not on top level submission
            "max_score": 2.0, // optional
            "name": "Your name here", // optional
            "number": "1.1", // optional (will just be numbered in order of array if no number given)
            "output": "Giant multiline string that will be placed in a <pre> tag and collapsed by default", // optional
            "tags": ["tag1", "tag2", "tag3"] // optional
            "visibility": "visible" // Optional visibility setting
        },
        // and more test cases...
    ]
}
```

For Java and Python, we have helper libraries that integrate with
JUnit and unittest to produce this output format easily.

### Controlling Test Case Visibility

You can hide some or all test cases based on your desired conditions. Visibility
can be controlled by setting the "visibility" field at the top level for an
assignment, or for an individual test.

Options for the visibility field are as follows:

- `hidden`: test case will never be shown to students
- `after_due_date`: test case will be shown after the assignment's due date has passed
- `after_published`: test case will be shown only when the assignment is explicitly published from the "Review Grades" page
- `visible` (default): test case will always be shown

If an assignment level visibility setting is set, a test can override this
setting with its own visibility setting. For example, you may set
`"visibility":"after_due_date"` at the top level so that all tests are hidden
until after the submission deadline. Then, you can set an individual test to
have `"visibility":"visible"` if it should always be shown. For example, this
can be useful for pre-submission checks such as a test that checks whether the
student's code compiled successfully or not. Another possibility is having a
subset of tests always visible to guide students through the homework, while
keeping the set of tests that they will be graded on hidden until after the
assignment is due.

If test cases are hidden, students will not be able to see their total
score. Test cases with visibility set to `hidden` don't affect this, since they
should only be used for tests which don't contribute points to the total.
