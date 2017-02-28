atmosphere-include-startup
=========

This role will ensure that atmosphere is setup to 'auto-start' whenever the server is booted.
This role is intended to be executed as part of the 'deploy_stack' playbook in clank in the 'post_deployment' section.


Requirements
------------

N/A

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| foo                     | no       | false   | true, false               | example variable                         |
| bar                     | yes      |         | eggs, spam                | example variable                         |

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
