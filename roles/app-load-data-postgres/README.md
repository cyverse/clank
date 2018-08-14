app-load-data-postgres
======================

Load data into PostgreSQL from a SQL dump file

Requirements
------------

- postgresql

Role Variables
--------------

- `DATABASE_FILE_TO_BE_LOADED`

Dependencies
------------


Example Playbook
----------------

```
    - hosts: servers
      roles:
        - { role: app-load-data-postgres,
            DBNAME: "{{ ATMO_DBNAME}} ",
            DATABASE_FILE_TO_BE_LOADED: "{{ SQL_DUMP_FILE }}" }
```

License
-------

BSD
