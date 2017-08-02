# CHANGELOG

## v?.?.? (2017-09-??)

- Change `INSTALLATION_TYPE` default from `development` to `production`
  ([#197](https://github.com/CyVerse/clank/pull/197))

## v2.0.0 (2016-08-17)
- Change logrotate file permissions to 644
  ([#109](https://github.com/CyVerse/clank/pull/109))
- Defines playbook for install/config of `nginx_novnc_auth` within atmosphere
  ([#104](https://github.com/CyVerse/clank/pull/104))
- Added conditional combined certification generation
  ([#102](https://github.com/CyVerse/clank/pull/102))
- Lograte conf file permissions
  ([#100](https://github.com/CyVerse/clank/pull/100))
- Added playbook to upgrade to new postgres
  ([#98](https://github.com/CyVerse/clank/pull/98))
- Changed `_format_output()` to always return a str
  ([#97](https://github.com/CyVerse/clank/pull/97))
- Removed roles no longer used by playbooks
  ([#96](https://github.com/CyVerse/clank/pull/96))
- Fixed issue with ssh system key generation on each execution
  ([#95](https://github.com/CyVerse/clank/pull/95))
- Fixed issue with ssl generation on each execution
  ([#94](https://github.com/CyVerse/clank/pull/94))
- Add official postgresql apt repository
  ([#92](https://github.com/CyVerse/clank/pull/92))
- Enable new relic
  ([#91](https://github.com/CyVerse/clank/pull/91))
- Fix pip install requirements
  ([#86](https://github.com/CyVerse/clank/pull/86))
- [v2.0] removed unused openstack_* settings
  ([#85](https://github.com/CyVerse/clank/pull/85))
- Removed unused openstack_* settings
  ([#84](https://github.com/CyVerse/clank/pull/84))
- Update readme.md
  ([#78](https://github.com/CyVerse/clank/pull/78))
- Add role call to change permissions
  ([#77](https://github.com/CyVerse/clank/pull/77))
- Add callback plugin for human readable error output
  ([#72](https://github.com/CyVerse/clank/pull/72))
- Propose different clank interface
  ([#71](https://github.com/CyVerse/clank/pull/71))
