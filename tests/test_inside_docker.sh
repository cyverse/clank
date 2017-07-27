#!/bin/sh -xe

yum install -y git python python-devel libffi-devel openssl-devel
yum install -y python-setuptools python-setuptools-devel
easy_install pip
yum groupinstall -y "Development tools"
pip install virtualenv
cd clank/
virtualenv clank_env
source clank_env/bin/activate
pip install -r requirements.txt
cp dist_files/variables.yml.dist variables.yml
clank_env/bin/python ./clank.py --env_file variables.yml -x "atmosphere_github_branch=\"${ATMO_GITHUB_BRANCH:-master}\"" -x "atmosphere_github_repo=\"${ATMO_GITHUB_REPO:-https://github.com/CyVerse/atmosphere.git}\"" -x "troposphere_github_branch=\"${TROPO_GITHUB_BRANCH:-master}\"" -x "troposphere_github_repo=\"${TROPO_GITHUB_REPO:-https://github.com/CyVerse/troposphere.git}\"" --skip-tags "distro-update,create-nginx-uwsgi,enable-services" -b