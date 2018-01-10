#!/usr/bin/env bash

cd /autograder/source

apt-get install -y python python-pip python-dev

mkdir -p /root/.ssh
cp ssh_config /root/.ssh/config
# Make sure to include your private key here
cp deploy_key /root/.ssh/deploy_key
# To prevent host key verification errors at runtime
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

# Clone autograder files
git clone git@github.com:gradescope/autograder_samples /autograder/autograder_samples
# Install python dependencies
pip install -r /autograder/autograder_samples/python/src/requirements.txt
