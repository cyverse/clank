app-backup-postgres
===================

Using PostgreSQL executables to dump the contents the database to a single file.

Requirements
------------

None.

Role Variables
--------------

- `database_names` - list of names of databases (defaults to `[]`)
- 'BACKUP_PATH' - a path that resides underneath the postgres user owernship
Dependencies
------------

None.

Example Playbook
----------------

If a specific database within the PostgreSQL server is not identified, a full backup will be made with `pg_dumpall` to a file named off the hostname of the server.

    - hosts: dbservers
      roles:
         - { role: app-backup-postgres,
             tags: ['atmosphere', 'data-backup', 'backup'] }

In addition to a full backup, a single file will be created for foreach string in `database_names`.

    - hosts: dbservers
      roles:
         - { role: app-backup-postgres,
             database_names: ["{{ DBNAME }}"],
             tags: ['atmosphere', 'data-backup', 'backup'] }

Or, you can list multiple databases by name

    - hosts: dbservers
      roles:
        - { role: app-backup-postgres,
            database_names: ['atmo_prod', 'troposphere'],
            tags: ['atmosphere', 'data-backup', 'backup'] }

Specifing a path for the dumps to be save to. Be sure that path given resides under the postgresql's owernship

    - hosts: dbservers
      roles:
        - { role: app-backup-postgres,
            BACKUP_PATH: /var/lib/postgresql/backups_are_important
            database_names: ['atmo_prod', 'troposphere'],
            tags: ['atmosphere', 'data-backup', 'backup'] }

License
-------

BSD

