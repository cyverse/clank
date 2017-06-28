tls-create-ca
=========

Create a certificate authority

The intention is that this playbook will **not** be used in production. It is
useful for local development but is otherwise a major liability.

Role Variables
--------------

Without any configuration the role will spit out: `ca_cert.pem` and
`ca_cert_key.pem` which are respectively the root cert and its private key.


| Variable               | Required  | Default               | Choices | Comment |
|------------------------|-----------|-----------------------|---------|---------|
| TLS_CA_CERT_DEST       | no        | ca_cert.pem           |         |         |
| TLS_CA_KEY_DEST        | no        | ca_cert_key.pem       |         |         |
| COUNTRY_NAME           | no        | US                    |         |         |
| STATE_OR_PROVINCE_NAME | no        | Arizona               |         |         |
| LOCALITY_NAME          | no        | Tucson                |         |         |
| ORGANIZATION_NAME      | no        | Organisation Name     |         |         |
| ORG_UNIT_NAME          | no        | Organisation Division |         |         |
| COMMON_NAME            | no        | Common Name CA        |         |         |
| EMAIL_ADDRESS          | no        | test@example.com      |         |         |

Example Playbook
----------------

    - hosts: localhost
      roles:
       - tls-create-ca

https://cyverse.org
