# Clank

Clank deploys the [Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) infrastructure within a Linux environment to make using OpenStack for on-demanding computing needs easy.

[Atmosphere](http://www.iplantcollaborative.org/ci/atmosphere) is made up of two distinct elements:
- an API: [_Atmosphere_](https://github.com/iPlantCollaborativeOpenSource/atmosphere)
- and, a user interface: [_Troposphere_](https://github.com/iPlantCollaborativeOpenSource/troposphere)

Clank is a set of playbooks & roles and is the replacement for [Crushbone](https://github.com/iPlantCollaborativeOpenSource/crushbone).

# License

See [LICENSE](LICENSE) file.

# Usage

```bash
python ratchet.py --workspace $WORKSPACE --env_file $VARIABLES_YML_FILE
```

And example of the [`$VARIABLES_YML_FILE`](dist_files/variables.yml.dist) can be found in the [dist_files](dist_files) directory.
