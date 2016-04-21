app-config-postgres
===================

Configure PostgreSQL per application needs.

Requirements
------------

- postgresql

Role Variables
--------------

- `DBNAME`
- `DBUSER`
- `DBPASSWORD`

Dependencies
------------

Example Playbook
----------------

```
    - hosts: all
      roles:
        - { role: app-config-postgres,
            DBNAME: "{{ ATMO_DBNAME }}",
            DBUSER: "{{ ATMO_DBUSER }}",
            DBPASSWORD: "{{ ATMO_DBPASSWORD }}"}
```

License
-------

BSD
