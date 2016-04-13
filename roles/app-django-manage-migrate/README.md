app-django-manage-migrate
=========================

Perform a data migration using Django Admin

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

- `APP_BASE_DIR`
- `VIRTUAL_ENV`
- `DJANGO_SETTINGS_MODULE`

Dependencies
------------

- `django_manage` module

Example Playbook
----------------

```
    - hosts: servers
      roles:
        - { role: app-django-manage-migrate,
            APP_BASE_DIR: "{{ TROPOSPHERE_LOCATION }}",
            VIRTUAL_ENV: "{{ VIRTUAL_ENV_TROPOSPHERE }}",
            DJANGO_SETTINGS_MODULE: 'troposphere.settings' }
```

License
-------

BSD
