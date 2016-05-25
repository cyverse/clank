logrotate-files
=========

A brief description of the role goes here.

Requirements
------------


Role Variables
--------------

- `LOGROTATE_FILES` - the logrotate file or list of files that will be linked to the logrotate file 

Dependencies
------------

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: all
      roles:
        - { role: logrotate-files,
            LOGROTATE_FILES: "{{ ATMOSPHERE_LOCATION }}/extras/logrotate.atmosphere",
            tags: ['atmosphere'] }
```

or

```
    - hosts: all
      roles:
        - { role: logrotate-files,
            LOGROTATE_FILES: "['{{ ATMOSPHERE_LOCATION }}/extras/logrotate.atmosphere','{{ ATMOSPHERE_LOCATION }}/extras/logrotate.celery']", 
            tags: ['atmosphere', 'celery'] }
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
