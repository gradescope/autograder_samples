# Getting Started

## Pre-requisites

If you haven't made an account on Gradescope, sign up as an instructor at
[Gradescope.com](https://gradescope.com/).

Programming assignments are part of [Gradescope Complete](https://gradescope.com/pricing),
so you'll need to either upgrade your course, or request trial access to the feature by
emailing [help@gradescope.com](mailto:help@gradescope.com).

You'll need to have a course set up, so create one if you don't have one.

## Setting Up Your Assignment

Navigate to the assignments tab on your course, and click on "Create
Programming Assignment" in the bottom bar.

[![Assignments](assignments.png)](assignments.png)

You'll be asked for some basic details about your assignment. Choose
the appropriate options and continue.

[![Assignment](assignment_form.png)](assignment_form.png)

Next you'll be asked to upload your autograder. Upload a zip file
meeting the required [specifications](specs), and press "Update
Autograder."

[![Configure Autograder](configure_autograder.png)](configure_autograder.png)

The page will reload and show you the Docker build output
as it sets up your image.

[![Build Status](build_status.png)](build_status.png)

Once the Docker image finishes building, you can click "Test
Autograder" to submit to the autograder yourself. You can use this to
debug the output of your autograder, and make sure everything is set
up correctly. You'll want to make sure your autograder is stable
before allowing students to submit.

[![Test Autograder](test_autograder.png)](test_autograder.png)

Once the release date arrives, students will be allowed to submit
their homework. They'll receive feedback as soon as the autograder
finishes running. You can control what feedback they receive in the
output file format. They'll see a list of test cases that they've
passed and failed, and any output you provide.

[![Student results](results.png)](results.png)
