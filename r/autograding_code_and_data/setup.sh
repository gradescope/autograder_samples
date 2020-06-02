#!/usr/bin/env bash

# or you can do it the slow way...
apt-get install -y libxml2-dev libcurl4-openssl-dev libssl-dev
apt-get install -y r-base

# these lines install the packages that is needed both
# 1. the student code 
# 2. the autograding code
Rscript -e "install.packages('gradeR')" 
Rscript -e "install.packages('stringr')" 
