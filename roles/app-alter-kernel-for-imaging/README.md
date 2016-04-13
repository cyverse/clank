app-alter-kernal-for-imaging
=========

Ensure target server has packages necessary to service Virtual Machine Imaging requests

Requirements
------------


Role Variables
--------------

- none

Dependencies
------------

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: app-alter-kernal-for-imaging, tag: ['atmosphere'] }
```

License
-------

BSD
