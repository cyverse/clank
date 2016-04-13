app-config-logging
==================

Creates & configures the logging directory of the application.

Requirements
------------

Role Variables
--------------

- `APP_BASE_DIR` - the base, or root, directory of the application
- `LOG_FILES` - either `'ATMO_LOG_FILES'` or `'TROPO_LOG_FILES'` (from `default/main.yml`)

Dependencies
------------

Example Playbook
----------------

```
    - hosts: all
      roles:
        - { role: app-config-logging,
            APP_BASE_DIR: '/vagrant/super/awesome',
            LOG_FILES: "{{ ATMO_LOG_FILES }}",
            tags: ['logging']}
```

License
-------

BSD
