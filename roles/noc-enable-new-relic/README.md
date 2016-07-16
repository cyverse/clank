Role Name
=========

Enables necessary settings for New Relic agents to run on service start.

This is part of network operations center activities (aka - monitoring) and, thus, has a "noc" prefix to the role name.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

- `ATMO_HOME` - defaults to `/opt/dev/atmosphere`
- `TROPO_HOME` - defaults to `/opt/dev/troposphere`
- `LOCAL_SETTINGS` - defaults to `settings/local.py`

Dependencies
------------

None.

Example Playbook
----------------

This role will fail is the local settings file is not present. It should be run after the local settings files for Atmosphere & Troposphere have been generated.

    - hosts: servers
      roles:
         - { role: noc-enable-new-relic }

If your installation uses a different location then the `/opt/dev` root directories, you need to pass in values for `ATMO_HOME` and `TROPO_HOME`:

    - hosts: servers
      roles:
         - { role: noc-enable-new-relic,
             ATMO_HOME: '/non-standard/atmo',
             TROPO_HOME: 'non-standard/tropo' }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
