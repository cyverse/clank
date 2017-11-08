setup-postgres
==================

Configure postgres for a user and port and ensure that only this postgres
version is running

Requirements
------------

## Role Variables

| Variable     | Required   | Default    | Choices   | Comments                           |
|--------------|------------|------------|-----------|------------------------------------|
| DB_USER      | no         | postgres   |           | User that is granted password auth |
| DB_VERSION   | no         | 9.6        |           | Postgres version                   |
| DB_PORT      | no         | 5432       |           | Database port                      |

Dependencies
------------

Example Playbook
----------------

```
    - hosts: all
      roles:
        - { role: setup-postgres }
```
