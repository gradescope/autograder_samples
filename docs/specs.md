# Autograder Specifications

Autograders are uploaded to Gradescope in zip format. The file must
contain at least two files in the root of the archive:

- **setup.sh**: a setup (Bash) script that installs all your dependencies. We're
  running on Ubuntu 18.04 images, so you can use apt, or any other means of
  setting up packages.

- **run_autograder**: an executable script, in any language (with
  appropriate `#!` line), that compiles and runs your autograder suite
  and produces the output in the correct place.

**Note**: When you are zipping up your files, make sure to zip the files, and not the folder containing the files. If you zip up the folder then the required files won't be at the root of the zip archive, but rather under a subdirectory, so we won't be able to find them. See the image below for a demonstration of the correct approach on MacOS.

[<img src="../zipping_files.png" width="619px" />](zipping_files.png)

## File hierarchy

All autograder related files will be in the /autograder directory. This directory structure is set up when the autograder Docker image is built.

When the autograder executes, the working directory is **/autograder**.

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
{ "score": 44.0, // optional, but required if not on each test case below. Overrides total of tests if specified.
  "execution_time": 136, // optional, seconds
  "output": "Text relevant to the entire submission", // optional
  "visibility": "after_due_date", // Optional visibility setting
  "stdout_visibility": "visible", // Optional stdout visibility setting
  "extra_data": {}, // Optional extra data to be stored
  "tests": // Optional, but required if no top-level score
    [
        {
            "score": 2.0, // optional, but required if not on top level submission
            "max_score": 2.0, // optional
            "name": "Your name here", // optional
            "number": "1.1", // optional (will just be numbered in order of array if no number given)
            "output": "Giant multiline string that will be placed in a <pre> tag and collapsed by default", // optional
            "tags": ["tag1", "tag2", "tag3"], // optional
            "visibility": "visible", // Optional visibility setting
            "extra_data": {} // Optional extra data to be stored
        },
        // and more test cases...
    ],
  "leaderboard": // Optional, will set up leaderboards for these values
    [
      {"name": "Accuracy", "value": .926},
      {"name": "Time", "value": 15.1, "order": "asc"},
      {"name": "Stars", "value": "*****"}
    ]
}
```

For Java and Python, we have helper libraries that integrate with
JUnit and unittest to produce this output format easily.

### Controlling Test Case Visibility

You can hide some or all test cases based on your desired conditions. Visibility
can be controlled by setting the "visibility" field at the top level for an
assignment, or for an individual test.

Note: Instructors will always see all tests, so for now you'll have to create a
student account to test visibility settings.

Options for the visibility field are as follows:

- `hidden`: test case will never be shown to students
- `after_due_date`: test case will be shown after the assignment's due date has passed. If late submission is allowed, then test will be shown only after the late due date.
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
score.

### Controlling standard output visibility

By default, anything printed to standard output is recorded and only shown to
instructors, for debugging purposes. If you know that nothing sensitive or
revealing is printed to standard output, you can make that content visible to
students by adding a top-level `"stdout_visibility"` key to your JSON. The value
should be one of `hidden`, `after_due_date`, `after_published`, or `visible`,
depending on when you want stdout to be visible to students. These options
mirror the test case visibility options described above.

### Leaderboards

You can add a "leaderboard" section to create leaderboards for your
assignment. You can [read more about leaderboards here](https://gradescope-autograders.readthedocs.io/en/latest/leaderboards/).
