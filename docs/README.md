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

# Pricing

The autograder platform is available with paid school site licenses
and for individual courses that pay for access to our "Gradescope
Complete" tier (see our [pricing page](https://www.gradescope.com/pricing)
for more information).

If you're an existing user or have any questions regarding pricing,
please contact us at
[help@gradescope.com](mailto:help@gradescope.com). If you want to
experiment with the platform to see if it works for you, feel free to
contact us for trial access.
