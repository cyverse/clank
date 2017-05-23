# HACKING.md

Generally, new roles should be created using [ansible-role-template](https://github.com/cyverse-ansible/ansible-role-template), using Ansible Galaxy and Travis CI as detailed [here](https://pods.iplantcollaborative.org/wiki/display/csmgmt/Ansible+at+CyVerse#AnsibleatCyVerse-AnsibleGalaxyRoles) (only visible to CyVerse staff).


## Quickly test a role against localhost without any variables/hosts/etc

First navigate into the role's main folder and run:
```
ANSIBLE_NOCOWS=1 ANSIBLE_ROLES_PATH="$(pwd)/.." ansible-playbook /dev/stdin -i "localhost," -c local <<EOF
---
- hosts: localhost
  roles:
      - $(basename $(pwd))
EOF
```
