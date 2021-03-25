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

## Running autograder images locally

To run your autograder image locally, you will currently need to bypass our
autograder harness because otherwise it will try to communicate with Gradescope
by default. You can do this by mounting a sample submission into the
`/autograder/submission` directory and then running `/autograder/run_autograder`
directly. Here's an example command; replace the path to the submission and
Docker image name with the appropriate values.

```bash
docker run --rm -v /path/to/submission:/autograder/submission username/image_name:tag bash -c "mkdir /autograder/results && /autograder/run_autograder && cat /autograder/results/results.json"
```

or to start an interactive session:

```bash
docker run --rm -it -v /path/to/submission:/autograder/submission username/image_name:tag bash
```

Minor notes:

- `--rm` is added to clean up the container after it exits. You can remove it if
  you want to inspect container logs or state afterwards.
- The `/autograder/results` directory is ordinarily created by the harness, so
  that's why you need to mkdir it. When running an interactive bash session you
  will need to create it too.
- In the first example, we're using `bash -c "..."` to run multiple commands in
  one Docker command and then show the results.
