[![Documentation Status](https://readthedocs.org/projects/gradescope-autograders/badge/?version=latest)](https://gradescope-autograders.readthedocs.org/en/latest/?badge=latest)

# Overview

Gradescope provides a language-agnostic platform for running your
autograders on our infrastructure. By running in Docker containers, we
give you full flexibility in setting up whatever language, compilers,
libraries, or other dependencies you need for your programming
assignments. You provide us with a setup script and an autograder
script, along with whatever supporting code you need, and we manage
accepting student submissions, running your autograder at scale, and
distributing the results back to students and to you.

!!! note "Updates"
    Our autograder platform is under active development! Check out the
    [Updates](updates/) page to see what we've changed recently.

# How it works

As an instructor, you create a new assignment on Gradescope, and
upload your autograder zip file following our
[specifications](https://gradescope-autograders.readthedocs.io/en/latest/specs/). Your code produces output in the format we
request. Students submit to Gradescope and have their work evaluated
on demand. They can submit as many times as they want. At the end of
the process, you can download their code and their results.

Follow our **[instructions](https://gradescope-autograders.readthedocs.io/en/latest/getting_started/)** to get started with
autograding.

# Examples

If you want to jump right in, we have built the following examples for
autograders in different languages. You can see how they are built,
and use them as a starting point for your own autograders. If you have
any further questions, feel free to contact us at
[help@gradescope.com](mailto:help@gradescope.com)

- [Python](python/)
- [Java (JUnit)](java/)
  - [Java+Maven](java-mvn/)

# Getting Help

If you need any help getting set up with the autograder platform,
please contact us at
[help@gradescope.com](mailto:help@gradescope.com). Please include as
much detail as possible, such as the programming language you're
trying to use, what you've tried, what errors you are seeing,
etc. Please also include a link to the assignment on Gradescope.

You can also ask questions on the [GitHub discussions
forum](https://github.com/gradescope/autograder_samples/discussions)
for this project, especially if there is no private information in
your question.

Issues regarding setup or installation of packages are often not
Gradescope specific. In general, information about installing packages
on our base operating system (currently Ubuntu 22.04 by default) will
be relevant to Gradescope. If you get errors during your autograder
setup phase it may help to search for those errors on Google or Stack
Overflow.

Given the multitude of software packages that are in use on the
Gradescope autograder platform, the Gradescope team is not intimately
familiar with each package's setup and configuration. When trying to
install or use packages, it is a good idea to check the package's
installation instructions or source code repository for any tips on
installing on Ubuntu 22.04, or instructions on configuration and
usage. It is also helpful to contact the authors of such packages when
possible because they will be more familiar with their own code.

# Pricing

The code autograder platform is available with an Institutional license or Institutional Trial.
If you have any questions regarding pricing, please contact us at sales@gradescope.com.
