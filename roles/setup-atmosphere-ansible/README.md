setup-atmosphere-ansible
========================

Installs atmosphere-ansible, an ansible installation used for instance
deployment.

Requirements
------------


Role Variables
--------------

- `BASE_DIR` - the directory of an existing atmosphere-ansible project
- `HOSTS` - a dictionary used to template atmosphere-ansible hosts file
- `GROUP_VARS` - a dictionary used to template atmosphere-ansible group_vars files
- `ANSIBLE_CONFIG` - a dictionary used to template atmosphere-ansible ansible.cfg


Dependencies
------------

Example Playbook
----------------

```
    - hosts: servers
      roles:
        - { role: setup-atmosphere-ansible,
            BASE_DIR: "/opt/dev/atmosphere-ansible"
            HOSTS:
               cloud1: |
                  127.0.0.1 ansible_ssh_port 22
                  192.168.0.3 ansible_ssh_port 22
            GROUP_VARS:
               cloud1: |
                  NTP_SERVERS:
                    - 0.us.pool.ntp.org

                  F2B_IGNOREIP:
                    - 127.0.0.1/8

            ANSIBLE_CONFIG:
                ANSIBLE_LOG_DIR: "/opt/dev/atmosphere/logs"
                ANSIBLE_FACT_CACHE_BACKEND: redis
                ANSIBLE_FACT_CACHE_TIMEOUT: 14400
                ANSIBLE_MANAGED_STR: "Ansible managed: {file} modified on %Y-%m-%d %H:%M:%S by {uid} on {host}"
                ANSIBLE_SSH_TIMEOUT: 10
                SUBSPACE_PLUGINS_DIR: "/opt/env/atmo/lib/python2.7/site-packages/subspace/plugins"
                SUBSPACE_CALLBACK_WHITELIST: play_logger
                SUBSPACE_COW_SELECTION: random
                SUBSPACE_NO_COWS: 1 }

```
