# Clank

Clank deploys the [Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) infrastructure within a Linux environment to make using OpenStack for on-demanding computing needs easy.

[Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) is made up of two distinct elements:
- an API: [_Atmosphere_](https://github.com/iPlantCollaborativeOpenSource/atmosphere)
- and, a user interface: [_Troposphere_](https://github.com/iPlantCollaborativeOpenSource/troposphere)

Clank is a set of playbooks & roles and is the replacement for [Crushbone](https://github.com/iPlantCollaborativeOpenSource/crushbone).

# License

See [LICENSE](LICENSE) file.

# Usage

```bash
python ratchet.py --workspace $WORKSPACE --env_file $VARIABLES_YML_FILE
```

And example of the [`$VARIABLES_YML_FILE`](dist_files/variables.yml.dist) can be found in the [dist_files](dist_files) directory.

####List of Files Needed Before Hand

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
* A publice id_rsa file

######Atmosphere and Troposphere DB FILES TO BE LOADED (Not required)
* atmosphere.sql
* troposphere.sql

Be sure to include the location of these files in your completed variables.yml.
