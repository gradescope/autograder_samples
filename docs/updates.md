# Updates

Here are some updates we've made to our autograder platform. If you have any questions or issues with any of these changes, please email [help@gradescope.com](mailto:help@gradescope.com).

## Nov 8th, 2022

We have upgraded `openssl` to 3.0.2-0ubuntu1.7 on Ubuntu 22.04 autograder images.
See [https://ubuntu.com/security/notices/USN-5710-1](https://ubuntu.com/security/notices/USN-5710-1) for more information.

## Aug 22nd, 2022

We have added the Fedora 36 and Rocky 8 base images.

## Aug 16th, 2022

We have added the ability to specify whether a test case should be considered to have passed or failed, overriding the default styling. See [our documentation on the results.json format](../specs#test-case-status) to learn more.

## Aug 3rd, 2022

We have updated the default autograder base image to Ubuntu 22.04, the current LTS release of Ubuntu. This will make newer versions of packages available to install.

If you experience any issues, such as autograders failing to build or failing to execute, you can revert to the previous version, which is Ubuntu 18.04. See [our documentation about base images here](../base_images).

## July 13th, 2022

We have added the ability to set the base image you want your autograder to build with. This means you are no longer required to build your own Docker container and use the manual docker configuration for zip file autograders which need a different base image. You can [find out more about base images here](../base_images).

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
	- See our [help documentation](../python3_issues) if you suspect this is causing issues with your autograder setup.
