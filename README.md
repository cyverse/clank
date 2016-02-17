*****
Clank
*****

Clank deploys the [Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) infrastructure within a Linux environment to make using OpenStack for on-demanding computing needs easy.

[Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) is made up of two distinct elements:
- an API: [_Atmosphere_](https://github.com/iPlantCollaborativeOpenSource/atmosphere)
- and, a user interface: [_Troposphere_](https://github.com/iPlantCollaborativeOpenSource/troposphere)

Clank is a set of playbooks & roles and is the replacement for [Crushbone](https://github.com/iPlantCollaborativeOpenSource/crushbone).

======================
Dependencies and Setup
======================

```bash
apt-get install python-virtualenv -y
apt-get install git python-dev libyaml-dev -y

git clone https://github.com/iPlantCollaborativeOpenSource/clank.git

virtualenv ratchet_env
. ratchet_env/bin/activate
pip install -r clank/ratchet_requirements.txt
```

=====
Usage
=====

```bash
python ratchet.py --env_file $VARIABLES_YML_FILE
```

An example of the [`$VARIABLES_YML_FILE`](dist_files/variables.yml.dist) can be found in the [dist_files](dist_files) directory.

###### Skipping Portions of Clank

Clank's install process is separated into three parts: installation of dependencies, atmosphere, troposphere.
To skip over sections of the deployment process, pass in a comma separated list to the `--skip` ratchet.py argument.

Supported skip tags: `dependencies`, `atmosphere`, `troposphere`

```bash
python ratchet.py --env_file $VARIABLES_YML_FILE --skip atmosphere # skips over the installation of atmosphere
```

```bash
python ratchet.py --env_file $VARIABLES_YML_FILE --skip dependencies,troposphere # skips over the installation of dependencies and troposphere
```

You can actually skip over any tag you may find in the roles and playbooks. Ratchet will pass the desired skips to ansible will skip those.


================================
List of Files Needed Before Hand
================================

######Completed variables.yml file

* variables.yml (See [variables dist](dist_files/variables.yml.dist) for blank template)

######Completed Ansible hosts file

* hosts (See [hosts dist](dist_files/hosts.dist) for blank template)

######Completed Ansible group_vars directory

* group_vars (See [group_vars dist](dist_files/group_vars) for blank template)

Your hosts file and group_vars should reflect one another. This would include renaming the dist file to relflect the groups you wish to create with ansible.

######SSL configuration files

* A organizational cert
* A bundle cert
* And a organization ssl key

######SSH keys configuration

* A private id_rsa file
* A public id_rsa file

######Atmosphere and Troposphere DB FILES TO BE LOADED (Not required)
* atmosphere.sql
* troposphere.sql

The location of these files *must* be stated in your _completed_ [variables.yml](https://github.com/iPlantCollaborativeOpenSource/clank/blob/master/dist_files/variables.yml.dist#L52-L63).

=======
License
=======
See [LICENSE](LICENSE) file.
