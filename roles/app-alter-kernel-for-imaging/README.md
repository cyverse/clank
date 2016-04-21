app-alter-kernel-for-imaging
============================

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
         - { role: app-alter-kernel-for-imaging, tag: ['atmosphere'] }
```

License
-------

BSD
