app-install-instance-deploy-automation
======================================

Installs Ansible playbooks used during instance deploy.

Note: _Atmosphere Ansible_ == "instance deploy automation"

Because the underlying technology of Clank is also *Ansible*, this role attempts to use a technology-agnostic term to indicate the purpose of this - to install the automation run on _"instance deploy"_ within Atmosphere.


Requirements
------------


Role Variables
--------------

- `APP_BASE_DIR` - the base, or root, directory of the Atmosphere API
- `SSH_PRIV_KEY` - the private key used by Atmosphere API to connect to virtual machines
- `SSH_PUB_KEY` - the public key injected into virtual machines launched by Atmosphere API
- `INSTANCE_DEPLOY_AUTOMATION_DIR` - directory of Atmosphere Ansible
- `INSTANCE_DEPLOY_AUTOMATION_HOSTS_FILE` - hosts file for Atmosphere Ansible
- `INSTANCE_DEPLOY_AUTOMATION_GROUP_VARS_FOLDER` - `group_vars` for Atmosphere Ansible


Dependencies
------------

Example Playbook
----------------

```
    - hosts: servers
      roles:
        - { role: app-install-instance-deploy-automation,
            APP_BASE_DIR: "{{ ATMOSPHERE_LOCATION }}",
            SSH_PRIV_KEY: "{{ ID_RSA }}",
            SSH_PUB_KEY: "{{ ID_RSA_PUB }}",
            INSTANCE_DEPLOY_AUTOMATION_DIR: "{{ ANSIBLE_DEPLOY_LOCATION }}",
            INSTANCE_DEPLOY_AUTOMATION_HOSTS_FILE: "{{ ANSIBLE_HOSTS_FILE }}",
            INSTANCE_DEPLOY_AUTOMATION_GROUP_VARS_FOLDER: "{{ ANSIBLE_GROUP_VARS_FOLDER }}",
            tags: ['ansible-deploy'] }
```


License
-------

BSD

