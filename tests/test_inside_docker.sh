#!/bin/sh -xe


ls -l /home

yum install -y git python python-pip python-devel libffi-devel openssl-devel
yum groupinstall "Development tools"
virtualenv clank_env
source clank_env/bin/activate
pip install -r requirements.txt
cp dist_files/variables.yml.dist variables.yml