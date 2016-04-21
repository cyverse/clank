build-install-troposphere-ui-assets
===================================

Does a build, bundle, and install for all assets associated with Troposphere User Interface

Requirements
------------

- Requires `nodejs` package to be installed

*Note:* this uses the `npm` executable which is included with `nodejs` package

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

- `NPM_APP_DIR` - the base directory the application
- `NPM_BUILD_TYPE` - the flavor ('production', 'dev') of the build; defaults 'production'
- `NPM_CLEAN_BUILD` - a boolean indicating it `node_modules` should be removed prior to build/bundle

Dependencies
------------


Example Playbook
----------------

```
    - hosts: servers
      roles:

        - { role: build-install-troposphere-ui-assets,
            NPM_APP_DIR: "{{ TROPOSPHERE_LOCATION }}",
            NPM_BUILD_TYPE: "{{ TROPOSPHERE_BUILD | default('production') }}",
            tags: ['troposphere', 'npm'] }
```

License
-------

BSD
