setup-postgres
==================

Configure pg_hba.conf & and ensure postgres is running 

Requirements
------------

Role Variables
--------------

- `DBUSER` - user which needs access to the database 

Dependencies
------------

Example Playbook
----------------

```
    - hosts: all
      roles:
        - { role: setup-postgres,
            when: clean_target,
            DBUSER: "{{ TROPO_DBUSER }}",
            tags: ['dependencies', 'database'] }
```

License
-------

BSD
