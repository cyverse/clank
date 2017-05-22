# HACKING.md

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
