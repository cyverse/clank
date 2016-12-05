# Utility Playbooks

## upgrage_postgres.yml

> Added in [pull request 98](https://github.com/CyVerse/clank/pull/98)

> Note: playbook assumes _"controller"_ is the **target** (see arguments below `... -c local -i "localhost,"`)

```
ansible-playbook playbooks/utils/upgrade_postgres.yml \
  --flush-cache -c local -i "localhost," \
    -e "{pg_version: '9.5',  pg_version_old: '9.3', database_names: ['atmosphere', 'troposphere']}"
```


## install_novnc_auth.yml

This is a utility playbook to be install an optional component to enhance functionality of Atmosphere. The component is a transparent authentication proxy using Nginx to allow community members access to [noVNC](https://kanaka.github.io/noVNC/) running on an instance within the Atmosphere Cloud. 

### Requirements

- a valid "build_env" variables.yml for Atmosphere (described in Clank [README.md](https://github.com/CyVerse/clank#list-of-files-needed-before-hand); examples in [dist_files](https://github.com/CyVerse/clank/blob/master/dist_files/variables.yml.dist))
- `hosts` including `[novnc_proxy]` group

```
ansible-playbook playbooks/utils/install_novnc_auth.yml \
  -i hosts -e @/vagrant/clank_init/build_env/variables.yml
```

Example `hosts` file for a vagrant instance:
```
[novnc_proxy]
novnc ansible_ssh_host=192.168.72.31 ansible_ssh_port=22 ansible_ssh_user=root
```
