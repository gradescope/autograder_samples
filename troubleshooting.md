# Troubleshooting

## Common error messages

### Autograder terminated with 'Killed'

If you see the word 'Killed' at the end of your autograder run, and it gets
terminated abruptly, this likely means that your autograder was terminated due
to exceeding the default memory limit for a single container. Our default memory
limit is 384MB, but we can increase this for you if you find that it's
necessary. Let us know if this is the case, and we'll take care of that for you.

### Your submission timed out

We have a default overall timeout of 20 minutes. If your autograder script takes
longer than that on our platform, it'll be forcibly terminated to avoid clogging
resources. To avoid running into our global timeout, we recommend adding
timeouts to your individual test cases - that'll at least allow your students to
receive a partial score for the parts that do terminate in a reasonable time
span. If they are subject to the global timeout, the submission will receive a 0
and, they won't see which tests were able to run successfully.

Keep in mind that on our autograder cluster, multiple tasks are running
concurrently. By default, each autograder is allocated 1/4 of a virtual CPU, so
you should adjust your running time expectations accordingly. The easiest way to
do this is to simply time how long your solution code takes to run.

If you need a longer timeout, let us know and we may potentially increase the
global timeout for your assignment. We can also increase the CPU allocation if
it's a CPU-intensive assignment.

### The autograder failed to execute correctly

This error message is returned when the autograder does not produce a valid JSON
file in `/autograder/results/results.json`. This could either mean that no such
file exists, or that the JSON is malformed.

Make sure your JSON output is not being interleaved with print statements from
within your autograder code or student code. The safest way to write your JSON
is to build up the JSON object structure as your tests run, and then write it to
the file at once, rather than outputting partial JSON strings to standard output
and then redirecting standard output to `/autograder/results/results.json`. The
latter is helpful when debugging your script locally, but for production use
it's not ideal because any print statements will break the JSON structure.


## Contact us!

If you have any further questions, feel free to contact us
at [help@gradescope.com](mailto:help@gradescope.com). Please mention Autograder
in the subject line, it'll help us automatically categorize the type of support
request.
