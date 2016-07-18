Role Name
=========

Enables necessary settings for New Relic agents to run on service start.

This is part of network operations center activities (aka - monitoring) and, thus, has a "noc" prefix to the role name.

Requirements
------------

Will only execution if there is a `NEW_RELIC` variable included.

The expected structure of this appears below:
```
NEW_RELIC:
    LICENSE: a1number30m3h43h00000000000
    ATMO_LABEL: 'Atmosphere Python (atmobeta)'
    TROPO_LABEL: 'Troposphere Python (atmobeta)'
    ENVIRONMENT: 'atmobeta'
    BROWSER: 'partials/__new_relic_browser.html'
```

Role Variables
--------------

- `TARGET_HOME` - **required**; defaults to emtpy, example: `/opt/dev/atmosphere`
- `MODULE_NAME` - **required**; defaults to empty, example `atmosphere`
- `LOCAL_SETTINGS` - defaults to `settings/local.py`
- `new_relic_app_name` - value used when generating `app_name` label for INI
- `new_relic_browser` - default to `False`, indicates if the New Relic Browser snippet should be included in `settings`

Dependencies
------------

None.

Example Playbook
----------------

This role will fail is the local settings file is not present. It should be run after the local settings files for Atmosphere & Troposphere have been generated.

    - hosts: servers
      roles:
         - { role: noc-enable-new-relic,
             TARGET_HOME: 'opt/dev/troposphere',
             MODULE_NAME: 'troposphere',
             new_relic_browser: True,
             new_relic_app_name: "{{ NEW_RELIC.TROPO_LABEL }}",
             tags: ['troposphere', 'new-relic', 'monitoring'] }

Or,

    - hosts: servers
      roles:
         - { role: noc-enable-new-relic,
             TARGET_HOME: 'opt/dev/atmosphere',
             MODULE_NAME: 'atmosphere',
             new_relic_app_name: "{{ NEW_RELIC.ATMO_LABEL }}" }

If your installation uses a different location then the `/opt/dev` root directories, you need to pass in values for `ATMO_HOME` and `TROPO_HOME`:

    - hosts: servers
      roles:
         - { role: noc-enable-new-relic,
             TARGET_HOME: '/non-standard/atmo',
             MODULE_HOME: 'atmosphere' }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
