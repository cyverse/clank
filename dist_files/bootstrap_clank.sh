#! /bin/bash

apt-get update
apt-get install -y git python python-pip python-dev libffi-dev libssl-dev
mkdir -p /opt/dev
cd /opt/dev
git clone --branch=master https://github.com/iPlantCollaborativeOpenSource/clank.git
cd ./clank
pip install -U pip virtualenv
virtualenv clank_env
. clank_env/bin/activate
pip install -r clank/requirements.txt
echo "You are now ready to run clank.py"
