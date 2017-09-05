Sanitary SQL Access for Atmosphere(2)
=========

Configures external read-only access to a subset of Atmosphere database (excluding secrets) for purposes of reporting/analytics and building development environments.

- cron script periodically produces a "sanitized dump" of database with secrets redacted
- Key-authed SSH access allowed as `sanitarysql` unix user
- `sanitarysql` unix user with login shell set to run script which dumps DB to stdout

Allow your developers and data scientists/analysts to run `ssh sanitarysql@my.atmo.cloud > db-dump.sql` and obtain a near-complete dump of Atmosphere(2) database. They can obtain a recent copy of production at any time without exposing secrets or obtaining any other kind of access to production environment. Using SSH in this way allows us to avoid exposing PostgreSQL server to the world (and worrying about PostgreSQL password auth, TLS, etc).

Role Variables
--------------

| Variable                  | Required | Default | Choices | Comments                                        |
|---------------------------|----------|---------|---------|-------------------------------------------------|
| atmosphere_database_name  | yes      |         |         | Should already be defined in clank vars         |
| SANITARY_SQL_SSH_KEYS     | yes      |         |         | List of SSH pub keys w/ access to sanitized DB  |


Example Playbook
----------------

    - hosts: all
      roles:
         - sanitary-sql-access

License
-------

See license.md

Author Information
------------------

Chris Martin
https://cyverse.org
