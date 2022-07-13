# Base Images

Gradescope support selecting a different base image to build your autograder with.

[![Base Image Selector](base_image_selector.png)](base_image_selector.png)

When you create a new autograder, it will default to the default base image. It is strongly recommend that you update your autograders to use the latest versions of the OS's which are supplied due to software deprecation and security updates on older versions of the OS.

Rebuilding an autograder or duplicating an autograder will use the same base image as was selected last.

## Base Image Selectors

### Base Image OS

This is the operating system which the base image is running (E.g. Ubuntu)

### Base Image Version

This is the version of the OS which is loaded in the base image (E.g. 18.04 for Ubuntu)

### Base Image Variant

This is to select pre-installed software in the base image to improve build time.

Selecting *Base* will mean that it is a fresh install of the OS with no modifications to the default installed programs.

Additional base images will be added which contain commly installed programs such as later versions of Python on older base images or Java on a base image. This should decrease the build time for those autograders.
