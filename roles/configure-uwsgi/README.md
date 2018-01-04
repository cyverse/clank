Configure uwsgi
=========

Template a uwsgi app

Requirements
------------

None

Role Variables
--------------

| Variable            | Required | Default    | Choices | Comments                                           |
|---------------------|----------|------------|---------|----------------------------------------------------|
| APP_NAME            | yes      |            |         | Ex. "atmosphere"                                   |
| APP_MODULE          | yes      |            |         | Ex. "atmosphere.wsgi"                              |
| APP_SRC_DIR         | yes      |            |         | Ex. "/opt/dev/atmosphere"                          |
| APP_VIRTUAL_ENV_DIR | yes      |            |         | Ex. "/opt/env/atmo"                                |
| APP_ENV_VARS        | no       | []         |         | Ex. ["DJANGO_SETTINGS_MODULE=atmosphere.settings"] |
| NUM_PROCESSES       | no       | 16         |         | For development, 2 is recommended                  |
| AUTORELOAD          | no       | false      |         | For development, true is recommended               |
| USER                | no       | "www-data" |         |                                                    |
| GROUP               | no       | "www-data" |         |                                                    |


`AUTORELOAD: true` will result in uwsgi restarting whenever the source for the
app changes.

Dependencies
------------

None

Example Playbook(s)
----------------
```
    - name: Configure atmosphere uwsgi for production
      hosts: all
      roles:
        - { role: configure-uwsgi,
            APP_NAME: 'atmosphere',
            APP_ENV_VARS: ["DJANGO_SETTINGS_MODULE=atmosphere.settings"],
            APP_SRC_DIR: "/opt/dev/atmosphere",
            APP_VIRTUAL_ENV_DIR : "/opt/env/atmo",
            APP_MODULE: "atmosphere.wsgi",

    - name: Configure atmosphere uwsgi for development
      roles:
        - { role: configure-uwsgi,
            APP_NAME: 'atmosphere',
            APP_ENV_VARS: ["DJANGO_SETTINGS_MODULE=atmosphere.settings"],
            APP_SRC_DIR: "/opt/dev/atmosphere",
            APP_VIRTUAL_ENV_DIR : "/opt/env/atmo",
            APP_MODULE: "atmosphere.wsgi",
            NUM_PROCESSES: 2,
            AUTORELOAD: true }
```
