setup-pyenv
=========

Install [pyenv](https://github.com/pyenv/pyenv) for python version control.


Role Variables
--------------
`PYTHON_VERSION`: The version of python to install and set as global python
default: 2.7.9

Dependencies
------------
None.

Example Playbook
----------------

```
---

- name: Install pyenv
  remote_user: root
  hosts: localhost
  roles:
    - setup-pyenv
```

Author Information
------------------

https://cyverse.org
