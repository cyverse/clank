Create nginx and uWSGI SSL files
=========

Runs make from extras/nginx, creates uwsgi directories and copies conf into place

At the end of execution, the required nginx ssl variables will be created and set as facts, or used in the location provided.

This role is different from its -nginx-uwsgi sister because it will save either one to a single destination, listed in the defaults

Requirements
------------


Role Variables
--------------

- `APP_BASE_DIR` - the base, or root, directory of the application
- `UWSGI_APP_NAME` - the name of the enabled UWSGI application
- `UWSGI_APPS_ENABLED_PATH` - path to enabled apps, default `/etc/uwsgi/apps-enabled/`
- `UWSGI_INI_SRC_NAME` (optional) - file name, including relative path from `APP_BASE_DIR`

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```
    - hosts: all
      roles:
        - { role: create-nginx-uwsgi,
            APP_BASE_DIR: "{{ TROPOSPHERE_LOCATION | default(troposphere_directory_path) }}",
            UWSGI_APP_NAME: 'troposphere',
            UWSGI_INI_SRC_NAME: 'extras/troposphere.uwsgi.ini',
            NGINX_SSL_KEY_PATH: "{{ SSL_KEY }}",
            NGINX_COMBINED_CERT_PATH: "{{ COMBINED_CERT }}",
            NGINX_SSL_KEY_DEST: "{{ TROPO.nginx.KEY_PATH }}",
            NGINX_COMBINED_CERT_DEST: "{{ TROPO.nginx.COMBINED_CERT_PATH }}",
            tags: ['troposphere'] }
```

or

```
    - hosts: all
      roles:
        - { role: create-nginx-uwsgi,
            APP_BASE_DIR: "{{ ATMOSPHERE_LOCATION | default(atmosphere_directory_path) }}",
            UWSGI_APP_NAME: 'atmosphere',
            UWSGI_INI_SRC_NAME: 'extras/uwsgi/atmo.uwsgi.ini',
            NGINX_SSL_KEY_PATH: "{{ SSL_KEY }}",
            NGINX_COMBINED_CERT_PATH: "{{ COMBINED_CERT }}",
            NGINX_SSL_KEY_DEST: "{{ ATMO.nginx.KEY_PATH }}",
            NGINX_COMBINED_CERT_DEST: "{{ ATMO.nginx.COMBINED_CERT_PATH }}",
            tags: ['atmosphere'] }
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
