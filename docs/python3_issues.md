# Python 3 issues

In September 2020, we upgraded our autograder base image to use Python
3 for our autograder harness.

If you're having issues with your Python 3 autograder not starting and
you're overriding the system version of `python3`, it may be occurring
because you have overridden the system `python3` executable. Since
Gradescope uses `python3` for our harness, we need to ensure that we
have the correct dependencies installed, and if the system `python3`
executable is overridden, this may no longer be the case. There are a
few possible ways to handle this situation.

If you have any trouble with these approaches, please contact
[help@gradescope.com](mailto:help@gradescope.com?subject=Python 3
autograder issues) and we'll help you get your autograder working.

## Update your autograder to use an explicit version of python3

Instead of overriding the sytem `python3` executable, you should be
able to refer to an explicit Python version in your code. E.g., if you
are installing `python3.8`, instead of overriding `python3` you can
use `python3.8` explicitly in your scripts (e.g. in your
`run_autograder` script, in any [#!
lines](https://en.wikipedia.org/wiki/Shebang_(Unix)), etc).

You will need to install packages by using `python3.8 -m pip ...`
instead of using `pip3`, since that would install packages in the
default system version of `python3`.

This is the preferred approach to solving this issue, and should be
most resilient in the long-term.

## Only alias python3 within your run_autograder script

If it's easier to continue using the `python3` executable name, you
could alias it within your `run_autograder` script, so that it does
not affect the rest of the system.

## Install Gradescope autograder harness dependencies

This approach is a little more brittle, but you can also work around
this issue by installing the dependencies our autograder harness needs
within your custom Python version. The current list of dependencies is
the following:

```
pyyaml pytz requests psutil grequests python-dateutil
```

You should be able to install these via `pip3` or by adding these
packages to your requirements.txt file.
