# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)

<!--
## [<exact release including patch>](<github compare url>) - <release date in YYYY-MM-DD>
### Added
  - <summary of new features>

### Changed
  - <for changes in existing functionality>

### Deprecated
  - <for soon-to-be removed features>

### Removed
  - <for now removed features>

### Fixed
  - <for any bug fixes>

### Security
  - <in case of vulnerabilities>
-->

## [Unreleased](https://github.com/cyverse/clank/compare/v33-0...HEAD) - YYYY-MM-DD
### Added
  - Add ability to configure allocation overrides
    ([#270](https://github.com/cyverse/clank/pull/270))

### Fixed
  - Fix the global http to https redirect in nginx
    ([#267](https://github.com/cyverse/clank/pull/267))
  - Fixed database loading ([#269](https://github.com/cyverse/clank/pull/269))

### Changed
  - Variable changes to DJANGO_DEBUG and SEND_EMAILS
    ([#271](https://github.com/cyverse/clank/pull/271))
  - Flattened TROPO_DATA and ATMO_DATA variables
    ([#273](https://github.com/cyverse/clank/pull/273))

## [v33-0](https://github.com/cyverse/clank/compare/v32-0...v33-0) - 2018-08-08
### Changed
  - Names of `group_vars` changed to use `ANSIBLE` in place of `SUBSPACE`
    ([#262](https://github.com/cyverse/clank/pull/262))

### Fixed
  - Tweaks for `sanitary-sql-access` role to work on all production
    deployments ([#261](https://github.com/cyverse/clank/pull/261))
  - Copy atmo deploy key from local secrets repo to target path
    ([#263](https://github.com/cyverse/clank/pull/263))

## [v32-0](https://github.com/cyverse/clank/compare/v31-0...v32-0) - 2018-04-23
### Added
  - Add 'kernel' tag, so that in a Docker context that tag can be skipped
    ([#255](https://github.com/cyverse/clank/pull/255))
  - Support multiple hostnames for Atmosphere(1) server
    ([#257](https://github.com/cyverse/clank/pull/257))

### Changed
  - Updated changelog format, i.e. to adopt process to update changelog per
    pull request ([#256](https://github.com/cyverse/clank/pull/256))
  - Database and configuration backups are stored in the same folder
    ([#258](https://github.com/cyverse/clank/pull/258))

### Fixed
  - Broken build resulting from lack of support for pip 10
    ([#259](https://github.com/cyverse/clank/pull/259))

## [v31-0](https://github.com/cyverse/clank/compare/v30-2...v31-0) - 2018-03-19
### Added
  - Configure nginx for different environments. Easily switch between uwsgi
    and dev servers

### Changed
  - Change service celery restart to gracefully wait for tasks to be finished,
    a second restart will trigger the workers to be forceful
  - Make the git clone task print which directories its cloning, when it fails
    because modifications exist you know which directory to inspect
  - Renamed several broad variables to be narrow and easier to configure
    properly
  - Upgraded to ansible 2.4

### Fixed
  - In the nginx config, uwsgi_params were not included, which broke the CAS
    callback
  - Fix broken `service celerybeat stop` command referred to undefined
    variable
  - Fixed incorrect queue names in the development celeryd config

## [v30-2](https://github.com/cyverse/clank/compare/v29-1...v30-2) - 2017-12-22
### Changed
  - Make atmosphere startup script less likely to bail

### Fixed
  - Create nginx/locations if they don't already exist
  - Include flower in nginx/locations
