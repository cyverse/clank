Reporting SQL Access for Atmosphere(2)
=========

Configures external read-only access to a subset of Atmosphere database (excluding secrets) for reporting/analytics purposes.

- `reporting` PostgreSQL role with read-only access to all information in Atmosphere database, except columns/tables containing 'sensitive' information
- Key-authed SSH access allowed as `reporting` unix user
- `reporting` unix user with login shell set to run script which dumps DB to stdout

Allow your data scientists/analysts to run `ssh reporting@my.atmo.cloud > db-dump.sql` and obtain a near-complete dump of Atmosphere(2) database for reporting/analytics purposes. They can take a live dump of production at any time without exposing secrets or obtaining any other kind of access to production environment. Using SSH in this way allows us to avoid exposing PostgreSQL server to the world (and worrying about PostgreSQL password auth, TLS, etc).

Role Variables
--------------

| Variable                  | Required | Default | Choices | Comments                                        |
|---------------------------|----------|---------|---------|-------------------------------------------------|
| atmosphere_database_name  | yes      |         |         | Should already be defined in clank vars         |
| reporting_access_ssh_keys | yes      |         |         | List of SSH public keys to get reporting access |


Example Playbook
----------------

    - hosts: all
      roles:
         - reporting-sql-access

License
-------

See license.md

Author Information
------------------

Chris Martin
https://cyverse.org
