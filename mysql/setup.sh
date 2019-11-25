#!/usr/bin/env bash

apt-get install -y python python-pip python-dev mysql-server

pip install -r /autograder/source/requirements.txt

# Start MySQL server
# will need to start again in run_autograder (this is just for importing data)
service mysql start
# Import test data
mysql < /autograder/source/database.sql
