delete-files
=========

Role to search and recursively delete files matching a location and glob 

Requirements
------------


Role Variables
--------------

- `LOCATION` - the location where you want to recursively search for a file matching the glob 
- `GLOB` - the glob you wish to search for file based off of

Dependencies
------------

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
      roles:
    - { role: delete-files,
        LOCATION: "/opt/dev/atmosphere",
        GLOB: "*.pyc",
        tags: ['atmosphere'] }
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
