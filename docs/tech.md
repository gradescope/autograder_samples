# Technical Details

Under the hood, we are using Docker to build a container image that is
used each time a student's submission needs to be graded. If you're
not familiar with Docker, think of it as a lightweight virtual
machine. Each container is isolated from others, and you can install
anything you want inside the container.

The image is based on **Ubuntu 18.04**, so packages can be installed with
apt, or from source or other means. The image is built once when you
set up your assignment, and each time students submit a new instance
of that image is spun up. 

Our autograder harness downloads the student's submission and puts it
in /autograder/submission, and then runs
**/autograder/run_autograder**. Once run_autograder has finished
running, the harness checks for output in
/autograder/results/results.json, and uploads these results to
Gradescope.
