app-django-manage-collectstatic
===============================

Perform a collect static resource operation using Django Admin

Requirements
------------


Role Variables
--------------

- `APP_BASE_DIR`
- `VIRTUAL_ENV`
- `DJANGO_SETTINGS_MODULE`
- `STATIC_DIR_PATH` (optional) - resolve path from `APP_BASE_DIR`


Dependencies
------------

- `django_manage`


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: all
      roles:
        - { role: app-django-manage-collectstatic,
            APP_BASE_DIR: "{{ TROPOSPHERE_LOCATION }}",
            VIRTUAL_ENV: "{{ VIRTUAL_ENV_TROPOSPHERE }}",
            STATIC_DIR_PATH: 'troposphere/tropo-static',
            DJANGO_SETTINGS_MODULE: 'troposphere.settings' }
```

License
-------

BSD
