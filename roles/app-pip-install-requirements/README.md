app-pip-install-requirements
============================

Install application requirements using `pip`


Requirements
------------

- `python-dev` (v2.7)
- `python-pip`


Role Variables
--------------

- `APP_BASE_DIR`
- `VIRTUAL_ENV`

These variables are used when building up the default `REQUIREMENTS_NAME`


Dependencies
------------

Intended to be used with `setup-virtualenv`.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: servers
      roles:
        - { role: setup-virtualenv,
            VIRTUAL_ENV_NAME: 'troposphere',
            VIRTUAL_ENV_BASE_DIR: "{{ VIRTUAL_ENV_DIR_TROPOSPHERE }}",
            tags: [ 'troposphere', 'setup-virtualenv'] }

        - { role: app-pip-install-requirements,
            APP_BASE_DIR: "{{ TROPOSPHERE_LOCATION }}",
            VIRTUAL_ENV: "{{ VIRTUAL_ENV_TROPOSPHERE }}",
            tags: ['troposphere']}
```


License
-------

BSD
