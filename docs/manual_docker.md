# Manual Docker Configuration

To use the "Manual Docker Configuration" option, you'll need to use
`gradescope/auto-builds` as the base image for your docker image.
You can also use the tags `fedora` or `centos`, or older versions of
Ubuntu - see the complete list [on DockerHub](https://hub.docker.com/r/gradescope/auto-builds/tags/).

You'll need to ensure that your image contains the `run_autograder` script at
the path `/autograder/run_autograder`. This should match the requirements
described on the [specifications](specs) page. In particular, at the end of the
script, the results should be in `/autograder/results/results.json` with the
correct formatting.

Any setup can be done in the Dockerfile, so there is no need for a `setup.sh`
script.

Beyond this, there are no other requirements on the structure of your Docker
image, so you can organize it as you wish.

## Private Docker Hub Repositories

If your Docker Hub repository is private, you'll need to give the user
`gradescopeecs` access to your repository. You may want to do this to
make sure that students cannot download your autograder image.
