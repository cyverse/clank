# RELEASE NOTES

## v2.0.0

This release removes the _helper_ script `ratchet.py` and replaces it with an executable script, `./clank.py`. The `ratchet_requirements.txt` has also be removed.

When upgrading, you will want to remove any lingering `ratchet_env`s that may exist with your deployed system.

The _helper_ script's replacement is `./clank.py`. It only needs a `-e` (short for _environment-file_) to be passed. We have removed the declaration of a `--workspace`.

Please refer to the updated [Usage](README.md#usage) section.

Features and improvements are noted in the [CHANGELOG](CHANGELOG.md).

Any problems discover, please log an [Issue](https://github.com/CyVerse/clank/issues).

## v1.0.0

Initial release.

### Contributors
- Andre Mercer
- Steve Gregory
- Matt DePorter
- Andrew Lenards
- Logo by Mariah Wall
