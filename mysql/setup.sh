#!/usr/bin/env bash

apt-get install -y python3 python3-pip python3-dev mysql-server

pip3 install -r /autograder/source/requirements.txt

# Start MySQL server
# will need to start again in run_autograder (this is just for importing data)
service mysql start
# Import test data
mysql < /autograder/source/database.sql
