atmosphere-include-startup
=========

This role will ensure that atmosphere is setup to 'auto-start' whenever the server is booted.
This role is intended to be executed as part of the 'deploy_stack' playbook in clank in the 'post_deployment' section.


Requirements
------------

N/A

Role Variables
--------------

N/A

Dependencies
------------

N/A

Example Playbook
----------------

    - hosts: all
      roles:
         - atmosphere-include-startup

License
-------

See license.md

Author Information
------------------
Steve Gregory
https://cyverse.org
