Role Name
=========

This role removes a path only if the path is a symlink

Requirements
------------

None

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

| Variable | Required | Default | Choices | Comments |
|----------|----------|---------|---------|----------|
| path     | yes      |         |         |          |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - { role: remove-symlink, path="/path/to/maybe/a/symlink" }

Or even better (as a task)

    - name: Remove symlink if it exists
      include_role:
      name: remove-symlink
        vars:
          path: "{{ some/variable }}"

License
-------

See license.md

Author Information
------------------

https://cyverse.org
