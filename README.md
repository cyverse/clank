![clanklogo](media/logoClank-01.png)

# Clank

Clank is a deployment tool for [Atmosphere](http://www.cyverse.org/atmosphere).


## Installation

Fetch packages required to build dependencies.
```bash
apt-get update
apt-get install -y git python python-pip python-dev libffi-dev libssl-dev
```

Fetch the repository.
```
git clone https://github.com/cyverse/clank.git
```

Prepare an environment for clank.
```
virtualenv clank_env
. clank_env/bin/activate
pip install -r clank/requirements.txt
```


## Usage

```bash
cd clank
./clank.py --env_file $VARIABLES_YML_FILE
```

An example of the [`$VARIABLES_YML_FILE`](dist_files/variables.yml.dist) can be found in the [dist_files](dist_files) directory.

### Running Portions of Clank

[WIP] -- All of clank should be re-evaluated to ensure that the 3 'supported tags' listed below cover enough ground. For now, ignore this section. -- [WIP]

Clank's install process is separated into three parts: installation of
dependencies, atmosphere, and troposphere. To run specific parts of the
deployment process, pass a comma separated list to the `--tags` option.

Supported tags: `dependencies`, `atmosphere`, `troposphere`

```bash
./clank.py --env_file $VARIABLES_YML_FILE --tags dependencies,troposphere
```

You can actually specify any tag you may find in the roles and playbooks. Clank
is a thin-wrapper over ansible.

### Passing extra arguments to ansible-playbook

Any arguments that Clank itself doesn't recognize will be passed to the resulting `ansible-playbook` run, which exposes the full capabilities of the `ansible-playbook` command. For example, if you have secrets that are encrypted with Ansible Vault, you can append `--ask-vault-pass` to your Clank command, and Ansible will prompt you for a password interactively.

## List of Files Needed Beforehand

### Completed variables.yml file

* variables.yml (See [variables dist](dist_files/variables.yml.dist) for blank template)

### Completed Ansible hosts file

* hosts (See [hosts dist](dist_files/hosts.dist) for blank template)  #FIXME: Bad path

### Completed Ansible group_vars directory

* group_vars (See [group_vars dist](dist_files/group_vars) for blank template)  #FIXME: Bad path

The hosts and group_vars files should reflect one another. This would include
renaming the dist file to relflect the groups you wish to create with ansible.

### SSL configuration files (Not required)

* A organizational cert
* A bundle cert
* And a organization ssl key

### SSH keys configuration (Not required)

* A private id_rsa file
* A public id_rsa file

### Atmosphere and Troposphere DB FILES TO BE LOADED (Not required)

* atmosphere.sql
* troposphere.sql

The location of these files *must* be stated in your _completed_
[variables.yml](https://github.com/iPlantCollaborativeOpenSource/clank/blob/master/dist_files/variables.yml.dist#L52-L63).  # FIXME: bad linked-lines.

## Contributing to clank

Generally, new roles should be created using [ansible-role-template](https://github.com/cyverse-ansible/ansible-role-template), using Ansible Galaxy and Travis CI as detailed [here](https://pods.iplantcollaborative.org/wiki/display/csmgmt/Ansible+at+CyVerse#AnsibleatCyVerse-AnsibleGalaxyRoles) (only visible to CyVerse staff).
k

## License

See [LICENSE](LICENSE) file.
