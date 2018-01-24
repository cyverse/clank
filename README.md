![clanklogo](media/logoClank-01.png)

# Clank  [![Build Status](https://travis-ci.org/cyverse/clank.svg?branch=master)](https://travis-ci.org/cyverse/clank)

Clank is a deployment tool for [Atmosphere](http://www.cyverse.org/atmosphere), written in [Ansible](http://ansible.com).

## Supported Operating Systems

At this time, Clank only supports deploying Atmosphere to Ubuntu 14.04. The deployment host which runs Clank can run any operating system which supports Ansible.

## Usage

### Installation

Clone the repository.
```
git clone https://github.com/cyverse/clank.git
```

Obtain Ansible of the version specified in `requirements.txt`. One way is to use a Python virtual environment, like this:

```
# Install Python dependencies if needed
apt-get update
apt-get install -y python python-pip python-dev libffi-dev libssl-dev python-virtualenv
# Create virtual environment, activate it, and install Ansible
virtualenv clank_env
. clank_env/bin/activate
pip install -r clank/requirements.txt
```

Install Ansible dependencies
```
ansible-galaxy install -f -r requirements.yml -p roles/
```

### Configuring Clank

#### Variables File

Clank is configured using a set of YAML variables which override default settings. See [dist_files/variables.yml.dist](dist_files/variables.yml.dist), which you can copy and customize for your deployment.

#### Target Host

By default, Clank is configured to deploy against localhost. To deploy to a remote target, modify the `hosts` file, replacing `localhost` with the desired target.

### Running Clank

```
ansible-playbook playbooks/deploy_stack.yml -e @/path/to/my/clank-variables.yml
```
To ensure you pick up the appropriate Ansible configuration, either run Clank from the root of this repository, or set the environment variable `ANSIBLE_CONFIG=/path/to/your/clank-repo/ansible.cfg`.

### Common Options

Skip some steps for a faster rebuild (after Clank has already run at least once):

`--skip-tags "clone-repo,data-load,npm,pip-install-requirements,apt-install"`

Verbose Ansible output for troubleshooting:

`-vvvvv -e "CLANK_VERBOSE=true" --tags print-vars`

All features of `ansible-playbook` are at your disposal, which can be viewed by running `ansible-playbook --help`.

### Optional Extra Functionality

Clank provides optional functionality that is used in some, but not all deployments. Enable these optional configurations by setting the corresponding variable to `true` (e.g. in your variables.yml).

| **Variable**               | **Purpose**                                                       |
|----------------------------|-------------------------------------------------------------------|
| SETUP_SANITARY_SQL_ACCESS  | external read-only access to subset of DB without secrets         |

### Running Portions of Clank

[WIP] -- All of clank should be re-evaluated to ensure that the 3 'supported tags' listed below cover enough ground. For now, ignore this section. -- [WIP]

Clank's install process is separated into three parts: installation of
dependencies, atmosphere, and troposphere. To run specific parts of the
deployment process, pass a comma separated list to the `--tags` option.

Supported tags: `dependencies`, `atmosphere`, `troposphere`

```bash
ansible-playbook playbooks/deploy_stack.yml -e @/path/to/my/clank-variables.yml --tags dependencies,troposphere
```

You can actually specify any tag you may find in the roles and playbooks. Clank
is just Ansible.

### Running Clank Utilities

Clank comes with several useful [utilities](playbooks/utils/README.md) located
in `playbooks/utils/`.

You can run a particular utility just like any other playbook:
```bash
ansible-playbook -e @/path/to/my/clank-variables.yml playbooks/utils/upgrade_postgres.yml
```

## Things you may wish to configure in your variables

### SSL configuration files (Not required)

* A organizational cert
* A bundle cert
* And a organization ssl key

### SSH keys configuration (Not required)

* A private id_rsa file
* A public id_rsa file

### Atmosphere and Troposphere database dump files (Not required)

* atmosphere.sql
* troposphere.sql

The location of these files *must* be stated in your _completed_
[variables.yml](https://github.com/CyVerse/clank/blob/master/dist_files/variables.yml.dist#L52-L63).  # FIXME: bad linked-lines.

### Custom Theme

You can change the images and colors used in [troposphere](https://github.com/cyverse/troposphere) to reflect your own institution's  branding.

#### Theme Images
To change images like the logo or favicon, add the absolute path to your theme images folder to the variable `THEME_IMAGES_PATH` in `variables.yml`.
```
THEME_MAGES_PATH: "/absoulte/path/to/your-images"
```
We recomened copying the `defaultThemeImages` folder found in Troposphere
`<projectRoot>/troposphere/static/theme/themeImagesDefault`

Replace any image in the folder with your new image keeping the same name and file type. It is important that the new image has the same dimensions and uses a transparent background or it may not display correctly. Your image may not be the same ratio as the image you are replacing but the file should be. For example, your logo might be shorter in length given the same height. Without distorting the logo ratio, align it to the left of the file and export the file at the same dimensions of the original file.


```
File Dimentions
+++++++++++++++++++++++++++
+--------------------     +
+| Logo Dimentions  |     +
+--------------------     +
+++++++++++++++++++++++++++
```
#### Theme Colors
To change the theme colors edit the color variable. Colors are used by cyverse-ui and Material-ui for components like buttons, toggles, radios, etc... See [Our Style Guide](https://cyverse.github.io/cyverse-ui/) for more information on how colors are used by components.

### Custom Nginx configuration
A developer of atmosphere/troposphere are going to be serving the app in unique ways. Often it's desired to serve assets that are generated whenever the source changes, so that developers can see changes as they're made. Sometimes it's useful to put interactive debuggers in the services. However the production nginx setup serves JS assets from a static folder, and daemonized python services via uwsgi.

Clank supports predefined nginx templates for common development workflows, which is configured via `nginx_locations`.

By default, the production value is:
```
nginx_locations: ["atmo-uwsgi", "tropo-uwsgi", "flower", "tropo-assets-path", "robots"]
```

This serves troposphere and the atmosphere api over uwsgi, includes an endpoint for
flower, serves troposphere assets from an asset directory on disk, and includes
an endpoint for robots.txt.

In order to serve troposphere assets from a webpack-dev-server instead of a
directory on disk, `nginx_locations` would include `"tropo-assets-server"`
instead of `"tropo-assets-path"`.
```
nginx_locations: ["tropo-assets-server", ...]
TROPO_ASSETS_SERVER_URL: "http://local.atmo.cloud:8080"
```

Note, that `TROPO_ASSETS_SERVER_URL` must be defined, and you will be
responsible for running the server at that location.

In order to serve the atmosphere api from a `./manage.py runserver` instance, `nginx_locations` would include `"atmo-dev-server"` instead of `"atmo-uwsgi"`.
```
LOCATIONS: ["atmo-dev-server", ...]
ATMO_DEV_SERVER_URL: "http://local.atmo.cloud:8000"
```

Note, that `ATMO_DEV_SERVER_URL` must be defined, and you will be responsible

In order to serve jenkins, `nginx_locations` would include `"jenkins"`.
```
LOCATIONS: ["jenkins", ...]
JENKINS_SERVER_URL: "http://127.0.0.1:8080"
```

Note, that `JENKINS_SERVER_URL` must be defined, and you will be
responsible for running the server at that location.

For further examples read the documentation of configure-nginx located
[here](./roles/configure-nginx/README.md).

## Contributing to clank

See [HACKING.md](./HACKING.md)

## License

See [LICENSE](LICENSE) file.
