![clanklogo](media/logoClank-01.png)

# Clank  [![Build Status](https://travis-ci.org/cyverse/clank.svg?branch=master)](https://travis-ci.org/cyverse/clank)

Clank is a deployment tool for [Atmosphere](http://www.cyverse.org/atmosphere).


## Installation

Fetch packages required to build dependencies.
```bash
apt-get update
apt-get install -y git python python-pip python-dev libffi-dev libssl-dev python-virtualenv

```

Fetch the repository.
```
git clone https://github.com/cyverse/clank.git
```

Prepare an environment for clank.
```
virtualenv clank_env
. clank_env/bin/activate
pip install -r clank/requirements.txt
```


## Usage

```bash
cd clank
./clank.py --env_file $VARIABLES_YML_FILE
```

An example of the [`$VARIABLES_YML_FILE`](dist_files/variables.yml.dist) can be found in the [dist_files](dist_files) directory.

### Running Portions of Clank

[WIP] -- All of clank should be re-evaluated to ensure that the 3 'supported tags' listed below cover enough ground. For now, ignore this section. -- [WIP]

Clank's install process is separated into three parts: installation of
dependencies, atmosphere, and troposphere. To run specific parts of the
deployment process, pass a comma separated list to the `--tags` option.

Supported tags: `dependencies`, `atmosphere`, `troposphere`

```bash
./clank.py --env_file $VARIABLES_YML_FILE --tags dependencies,troposphere
```

You can actually specify any tag you may find in the roles and playbooks. Clank
is a thin-wrapper over ansible.

### Running Clank Utilities

Clank comes with several useful [utilities](playbooks/utils/README.md) located
in `./playbooks/utils/*`.

To run a particular utility use the `--playbook` flag:
```bash
./clank.py -env_file $VARIABLES_YML_FILE --playbook playbooks/utils/upgrade_postgres.yml
```

### Passing extra arguments to ansible-playbook

Any arguments that Clank itself doesn't recognize will be passed to the resulting `ansible-playbook` run, which exposes the full capabilities of the `ansible-playbook` command. For example, if you have secrets that are encrypted with Ansible Vault, you can append `--ask-vault-pass` to your Clank command, and Ansible will prompt you for a password interactively.

## List of Files Needed Beforehand

### Completed variables.yml file

* variables.yml (See [variables dist](dist_files/variables.yml.dist) for blank template)

### SSL configuration files (Not required)

* A organizational cert
* A bundle cert
* And a organization ssl key

### SSH keys configuration (Not required)

* A private id_rsa file
* A public id_rsa file

### Atmosphere and Troposphere DB FILES TO BE LOADED (Not required)

* atmosphere.sql
* troposphere.sql

The location of these files *must* be stated in your _completed_
[variables.yml](https://github.com/CyVerse/clank/blob/master/dist_files/variables.yml.dist#L52-L63).  # FIXME: bad linked-lines.

## Custom Theme

You can change the images and colors used in [troposphere](https://github.com/cyverse/troposphere) to reflect your own institution's  branding.

### Theme Images
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
### Theme Colors
To change the theme colors edit the color variable. Colors are used by cyverse-ui and Material-ui for components like buttons, toggles, radios, etc... See [Our Style Guide](https://cyverse.github.io/cyverse-ui/) for more information on how colors are used by components.

## Contributing to clank

Generally, new roles should be created using [ansible-role-template](https://github.com/cyverse-ansible/ansible-role-template), using Ansible Galaxy and Travis CI as detailed [here](https://pods.iplantcollaborative.org/wiki/display/csmgmt/Ansible+at+CyVerse#AnsibleatCyVerse-AnsibleGalaxyRoles) (only visible to CyVerse staff).
k

## License

See [LICENSE](LICENSE) file.
