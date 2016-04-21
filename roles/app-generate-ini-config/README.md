app-generate-ini-config
=======================

Generate configuration file in INI format using application's `./configure` script

Requirements
------------

- Python `virtualenv`
- filter_plugin `to_ini`

Role Variables
--------------

- `template_vars`
- `APP_BASE_DIR`
- `VIRTUAL_ENV`
- `CLANK_VERBOSE`

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: servers
      roles:
        - { role: app-generate-ini-config,
            template_vars: "{{ TROPO }}",
            APP_BASE_DIR: "{{ TROPOSPHERE_LOCATION }}",
            VIRTUAL_ENV: "{{ VIRTUAL_ENV_TROPOSPHERE }}"}
```

License
-------

BSD
