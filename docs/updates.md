# Updates

Here are some updates we've made to our autograder platform. If you have any questions or issues with any of these changes, please email [help@gradescope.com](mailto:help@gradescope.com).

## July 13th, 2022

We have now added the ability to set the base image you want your autograder to build with via our front end app. This means you are no longer required to build your own docker container and use the manual docker configuration for zip file autograders which just needed a different base image. You can find more about it [here](base_image)

## March 17th, 2022

An upstream update to our underlying host OS introduced a conflict with the default Ubuntu 18.04 base image used for building autograders. For users installing certain packages that depend on glibc, this may have manifested in the build error below:

```
ERROR: Your kernel version indicates a revision number
of 255 or greater. Glibc has a number of built in
assumptions that this revision number is less than 255.
If you\'ve built your own kernel, please make sure that any
custom version numbers are appended to the upstream
kernel number with a dash or some other delimiter.
```

We have temporarily worked around this issue by building a new version of our base image. This should resolve the issue for now, until a more permanent fix is released by the Ubuntu team. Affected users will need to re-upload their autograder zip file to successfully update their autograder image.

## September 4th, 2020

- The Ubuntu, Fedora, and CentOS base images had their default Python installation upgraded from Python 2 to Python 3.
	- See our [help documentation](python3_issues) if you suspect this is causing issues with your autograder setup.
