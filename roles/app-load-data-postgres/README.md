app-load-data-postgres
======================

Load data into PostgreSQL from a SQL dump file

Requirements
------------

- postgresql

Role Variables
--------------

- `LOAD_DATABASE`
- `DATABASE_FILE_TO_BE_LOADED`

**Note:** `LOAD_DATABASE` remains so that when this role is composed into a
setup scenario it can still be overidden by a variable in `extra_vars`. It
likely will seem out-of-place, or unneeded. However, if a playbook (like, say,
`setup-troposphere.yaml`) wants to optionally avoid _data loading_, then having
it present in a parameterized manner gives the ability to skip the role.

Dependencies
------------


Example Playbook
----------------

```
    - hosts: servers
      roles:
        - { role: app-load-data-postgres,
            DBNAME: "{{ ATMO_DBNAME}} ",
            LOAD_DATABASE: True,
            DATABASE_FILE_TO_BE_LOADED: "{{ SQL_DUMP_FILE }}" }
```

License
-------

BSD
