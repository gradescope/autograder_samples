# Pulling Autograder from Git

To speed up autograder development, you can pull your autograder from a Git
repository. This will allow you to avoid long setup times when testing changes
to your autograder. You will still want to put common setup in your `setup.sh` or
`Dockerfile`, to avoid having to install things on each autograder run. You may
also want to include a copy of the repository in the base image, so that
autograder runs don't have to clone it from scratch.

If you just want to jump in, you can check out our
[example](https://github.com/gradescope/autograder_samples/tree/master/deploy_keys).
When using this, make sure to generate a keypair, and include your private key
file in your autograder zip file or Docker image.

## Setting up your SSH configuration

You should set up your ssh config so that Git knows to use the correct private
key when pulling. Your configuration should look something like the following:

```
Host github.com
  IdentityFile ~/.ssh/deploy_key
  IdentitiesOnly yes
```

Make sure to include the private key in your autograder image, and copy it to
the right place.

You should also make sure to include the host keys for your git server, so that
you don't get a host key verification error at runtime. You can do this by
running something like

```
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts
```

in your setup script.

## Github Deploy Keys

Github has a
[deploy keys](https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys)
feature, which allows you to set up a read-only key without a passphrase for the purpose of  pulling down your autograder. Follow their instructions on how to generate a new keypair, and add the public key to your Github repository. Then, you can configure SSH to use the private key when connecting to github.com as described above.
