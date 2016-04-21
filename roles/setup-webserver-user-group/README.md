setup-webserver-user-group
==========================

Add the "webserver_user" & configure owner permissions.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

- `APP_BASE_DIR` - the base, or root, of the application (where _owner_ is set)
- `WEBSERVER_USER` - name of the user associated with web server
- `VAGRANT` - indicate when operating within Vagrant; defaults to `False`

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
