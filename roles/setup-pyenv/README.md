setup-pyenv
=========

Install [pyenv](https://github.com/pyenv/pyenv) for python version control.

Role Variables
--------------

| Variable       | Required | Default      | Choices | Comments                                                  |
|----------------|----------|--------------|---------|-----------------------------------------------------------|
| PYTHON_VERSION | no       | 2.7.9        |         | The version of python to install and set as global python |
| PYENV_ROOT     | no       | /root/.pyenv |         | The directory where pyenv will live                       |

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
