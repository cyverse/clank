# ansible-uwsgi

Installs uWSGI

### Role Variables

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

| Variable                | Required | Default | Choices                   | Comments                                   |
|-------------------------|----------|---------|---------------------------|--------------------------------------------|
| PYTHON_VERSION          | yes      | 2.7.9   | Any version number        | Controls the version of python to use      |
| UWSGI_VERSION           | yes      | 2.0.15  | Any version number        | Controls the version of uWSGI to install   |
| INSTALL_ENV             | yes      | "/usr/local"|                       | Location to install uwsgi binary           |
