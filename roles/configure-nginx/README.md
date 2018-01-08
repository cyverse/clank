Configure nginx
=========

Template an nginx configuration that supports predefined locations

Nginx can be tricky to configure, so the hope is that predefining locations
will make useful workflows more accessible, see `LOCATIONS` and Common Use
Cases below.

Requirements
------------

None

Role Variables
--------------

| Variable                | Required | Default | Choices | Comments                                        |
|-------------------------|----------|---------|---------|-------------------------------------------------|
| LOCATIONS               | yes      | []      |         | See below for more info                         |
| SERVER_URL              | yes      |         |         | Ex. https://local.atmo.cloud                    |
| SSL_KEY                 | yes      |         |         | Path to the key for certificate                 |
| SSL_CERT                | yes      |         |         | Path to the full certificate chain              |
| SSL_CACHAIN_CERT        | no       |         |         | See below for more info                         |
| ENABLE_HTTP2            | no       | true    |         | Serve assets over http2                         |
| ENABLE_SSL_STAPLING     | no       | true    |         | See below for more info                         |
| ENABLE_STRICT_TRANSPORT | no       | true    |         | Instruct browser to only make https connections |
| TROPO_ASSETS_PATH       | no       |         |         | See below for more info                         |
| TROPO_ASSETS_SERVER_URL | no       |         |         | See below for more info                         |
| TROPO_DEV_SERVER_URL    | no       |         |         | See below for more info                         |
| ATMO_DEV_SERVER_URL     | no       |         |         | See below for more info                         |
| JENKINS_SERVER_URL      | no       |         |         | See below for more info                         |


`ENABLE_STRICT_TRANSPORT` instructs browsers to only accept valid HTTPS (see
[HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)). If
you're using self-signed certs you will want this to be false. If it was
previously true, you'll need to reset the HSTS entry in your browser.

`SSL_CACHAIN_CERT` is a path to the certificate authority chain, (i.e. full
chain - our cert), it is necessary when `ENABLE_SSL_STAPLING: true`.

`TROPO_ASSETS_PATH` is a path to a directory storing the troposphere build assets.
It is only necessary if the `tropo-assets-path` location is included. See the
common use case below.

`TROPO_ASSETS_SERVER_URL` is a URL which should identify a webpack dev server.
Clank will not start the server. See the common use case below.

`TROPO_DEV_SERVER_URL` is a URL which should identify a troposphere dev
server, namely a `./manage.py runserver` in /opt/dev/troposphere. This is
useful if you want to drop debugger statements in the python application.

`ATMO_DEV_SERVER_URL` is a URL which should identify an atmopshere api dev
server, namely a `./manage.py runserver` in /opt/dev/atmosphere. This is
useful if you want to drop debugger statements in the python application.

`JENKINS_SERVER_URL` is a URL which should identify a jenkins server.

`LOCATIONS` is a list of predefined nginx locations to include. You can use
this list to create an Nginx that serves troposphere assets from a dev server
or a static assets directory, serves the python applications from uwsgi or
local development servers, etc.

Some of the locations require additional variables to be defined. In any case,
this role is just setting up an nginx configuration it won't start a dev
server for you. The various services will need to be started manually (unless
another roles starts these for you).

Note that nginx will handle https, so each service should run over http
without a key or cert.

## Common Use Cases:
### In production
Serve troposphere and the atmosphere api over uwsgi, add an endpoint for
flower, serve troposphere assets from an asset directory on disk, and include
an endpoint for robots.txt.
```
TROPO_ASSETS_PATH: "/opt/dev/troposphere/troposphere/assets"
LOCATIONS: ["atmo-uwsgi", "tropo-uwsgi", "flower", "tropo-assets-path", "robots"]
```

### Running webpack-dev-server
Serve troposphere assets from a webpack-dev-server instead of a directory on
disk. This location would be used instead of `tropo-assets-path`.
```
TROPO_ASSETS_SERVER_URL: "http://local.atmo.cloud:8080"
LOCATIONS: ["tropo-assets-server", ...]
```

### Running an atmosphere dev server (./manage.py runserver)
Serve the atmosphere api from a `./manage.py runserver` instance. This
location would be used instead of `atmo-uwsgi`.
```
ATMO_DEV_SERVER_URL: "http://local.atmo.cloud:8000"
LOCATIONS: ["atmo-dev-server", ...]
```

### Running a troposphere dev server (./manage.py runserver)
Serve troposphere from a `./manage.py runserver` instance. This
location would be used instead of `tropo-uwsgi`.
```
TROPO_DEV_SERVER_URL: "http://local.atmo.cloud:3000"
LOCATIONS: ["tropo-dev-server", ...]
```

Example Playbook(s)
----------------
```
- name: Configure nginx for production
  hosts: all
  roles:
    - { role: configure-nginx,
        SERVER_URL: "https://atmo.cyverse.org",
        LOCATIONS: ["atmo-uwsgi", "tropo-uwsgi", "flower", "tropo-assets-path", "robots"],
        SSL_KEY: "/etc/ssl/private/local.atmo.cloud.key",
        SSL_CERT: "/etc/ssl/certs/local.atmo.cloud.fullchain.crt",
        SSL_CACHAIN_CERT: "/etc/ssl/certs/local.atmo.cloud.cachain.crt",
        TROPO_ASSETS_PATH: "/opt/dev/troposphere/troposphere/assets" }

- name: Configure nginx for development
  hosts: all
  roles:
    - { role: configure-nginx,
        SERVER_URL: "https://local.atmo.cloud",
        LOCATIONS: ["atmo-uwsgi", "tropo-uwsgi", "tropo-assets-path"],
        SSL_KEY: "/etc/ssl/private/local.atmo.cloud.key",
        SSL_CERT: "/etc/ssl/certs/local.atmo.cloud.fullchain.crt",
        ENABLE_SSL_STAPLING: false,
        ENABLE_STRICT_TRANSPORT: false,
        TROPO_ASSETS_PATH: "/opt/dev/troposphere/troposphere/assets" }
```
