# Manual Docker Configuration

If you are familiar with Docker, you can build your own Docker image and use it
on Gradescope instead of having Gradescope build your container image from a zip
file. This may be helpful if you want more control over how your image is
built. It will also allow you to take advantage of local Docker build caching to
speed up build times. It is not necessary to use this option to run your
autograders on Gradescope, but it is available as an advanced feature for those
who are familiar with the underlying container technology.

!!! note "Docker documentation"
    The rest of this page assumes familiarity with the Docker platform,
    including building a Docker image and pushing it to a Docker image
    registry such as DockerHub. For more information, please see the
    [official Docker documentation](https://docs.docker.com).

## Requirements

To use the "Manual Docker Configuration" option, you'll need to use
`gradescope/autograder-base` as the base image for your docker image.
You can also other operating systems such as `fedora`, or different versions of
Ubuntu - see the complete list [on DockerHub](https://hub.docker.com/r/gradescope/autograder-base/tags/).

Note: You can now also
[use different base images with a zip file upload](../base_images).

You'll need to ensure that your image contains the `run_autograder` script at
the path `/autograder/run_autograder`. This should match the requirements
described on the [specifications](../specs) page. In particular, at the end of the
script, the results should be in `/autograder/results/results.json` with the
correct formatting.

Any setup can be done in the Dockerfile, so there is no need for a `setup.sh`
script. You can use one if it's easier though.

Beyond this, there are no other requirements on the structure of your Docker
image, so you can organize it as you wish.

If you're just getting started, you can look at [our sample Dockerfile](https://github.com/gradescope/autograder_samples/tree/master/manual_docker).
This example puts all the autograder source in a `source` directory and uses a
`setup.sh` file similar to the zip file upload method, so it can be a good
transition path for going from a zip file to fully custom Docker builds.

You may also wish to refer to the [Dockerfile reference docs](https://docs.docker.com/engine/reference/builder/).

## Private Docker Hub Repositories

If your Docker Hub repository is private, you'll need to give the user
`gradescopeecs` access to your repository. You may want to do this to
make sure that students cannot download your autograder image.

## Running autograder images locally

To run your autograder image locally, you will currently need to bypass our
autograder harness because otherwise it will try to communicate with Gradescope
by default. You can do this by mounting a sample submission into the
`/autograder/submission` directory and then running `/autograder/run_autograder`
directly. Here's an example command; replace the path to the submission, results
directory, and Docker image name with the appropriate values.

```bash
docker run --rm -v /path/to/submission:/autograder/submission -v /path/to/results:/autograder/results username/image_name:tag /autograder/run_autograder && cat /path/to/results/results.json
```

or to start an interactive session:

```bash
docker run --rm -it -v /path/to/submission:/autograder/submission -v /path/to/results:/autograder/results username/image_name:tag bash
```

Minor notes:

- `--rm` is added to clean up the container after it exits. You can remove it if
  you want to inspect container logs or state afterwards.
- The `/autograder/results` directory should be mounted to a path on your host
  so that you can inspect the results.json file that your autograder produces.
