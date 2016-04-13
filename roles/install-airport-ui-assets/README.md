install-airport-ui-assets
=========================

Install resources of Airport UI (aka cf2) into assets location

Requirements
------------

- Valid path to a cloned repository on disk with the Airport UI resources.

Role Variables
--------------

- `AIRPORT_SOURCE` - the absolute path to the source code (aka resources) of Airport UI

Dependencies
------------

- None

Example Playbook
----------------

```
    - hosts: all
      roles:
         - { role: install-airport-ui-assets,
             AIRPORT_SOURCE: "{{ TROPOSPHERE_LOCATION }}" }
```

License
-------

BSD

