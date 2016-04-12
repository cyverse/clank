setup virtualenv
=========

Create a Python virtualenv

Requirements
------------

Python 2.7 must installed `python-dev` & `python-pip`

Role Variables
--------------

The following variables should be set when invoking this role:

* `VIRTUAL_ENV_NAME` - a project name, like 'atmo', used in building full path
* `VIRTUAL_ENV_BASE_DIR` - absolute path to the base directory of the virtual environment

**NOTE:** `VIRTUAL_ENV_BASE_DIR` will default to `/opt/env` which is used as a "canonical" path within the development of Atmosphere for virtual environments

Given the above variables, `VIRTUAL_ENV_FULL_PATH` will be the following:
```
VIRTUAL_ENV_FULL_PATH: "{{ VIRTUAL_ENV_BASE_DIR }}/{{ VIRTUAL_ENV_NAME }}"
```

Dependencies
------------
* No role dependency

Example Playbook
----------------

```
    - name: Example Usage
      hosts: all
      roles:
         - { role: setup-virtual-env, VIRTUAL_ENV_NAME: "atmo" }
```

License
-------

BSD
