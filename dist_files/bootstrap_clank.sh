#! /bin/bash

apt-get update
apt-get install -y git python python-pip python-dev libffi-dev libssl-dev
mkdir -p /opt/dev
cd /opt/dev
git clone --branch=master https://github.com/cyverse/clank.git
cd ./clank
pip install -U pip virtualenv
virtualenv clank_env
source /opt/dev/clank/clank_env/bin/activate
pip install -r /opt/dev/clank/requirements.txt
echo "You are now ready to run clank.py"
