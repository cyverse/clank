tls-create-csr
=========

Create a certificate signing request

The intention is that this playbook will **not** be used in production. It is
useful for local development but is otherwise a major liability.

Role Variables
--------------

There are two ways to set the necessary variables. If you're not sure what to
do just fill out this `DOMAIN_NAME` and the role will spit out
`server_cert_csr.pem` and `server_cert_key.pem` which are respectively the
cert request and private key for the cert awaiting to be signed.

| Variable                      | Required       | Default               | Choices       | Comment                                         |
|-------------------------------|----------------|-----------------------|---------------|-------------------------------------------------|
| DOMAIN_NAME                   | yes            |                       |               | Should be the fully qualified domain name       |
| TLS_CERT_REQUEST_DEST         | no             | server_cert_csr.pem   |               | Path to generated cert signing request          |
| TLS_CERT_PRIVATE_KEY_DEST     | no             | server_cert_key.pem   |               | Path to generated cert key                      |

Another route is to specify all of the following variables.

| Variable                        | Required          | Default                     | Choices       | Comment                                    |
|---------------------------------|-------------------|-----------------------------|---------------|--------------------------------------------|
| TLS_CERT_REQUEST_DEST           | no                | server_cert_csr.pem         |               | Path to generated cert signing request     |
| TLS_CERT_PRIVATE_KEY_DEST       | no                | server_cert_key.pem         |               | Path to generated cert key                 |
| COUNTRY_NAME                    | no                | US                          |               |                                            |
| STATE_OR_PROVINCE_NAME          | no                | Arizona                     |               |                                            |
| LOCALITY_NAME                   | no                | Tucson                      |               |                                            |
| ORGANIZATION_NAME               | no                | Organisation Name           |               |                                            |
| ORG_UNIT_NAME                   | no                | Organisation Division       |               |                                            |
| COMMON_NAME                     | no                | DOMAIN_NAME                 |               | If missing, requires DOMAIN_NAME           |
| EMAIL_ADDRESS                   | no                | test@example.com            |               |                                            |
| DNS_1                           | no                | DOMAIN_NAME                 |               | If missing, requires DOMAIN_NAME           |
| DNS_2                           | no                |                             |               |                                            |
| DNS_3                           | no                |                             |               |                                            |
| DNS_4                           | no                |                             |               |                                            |

Example Playbook
----------------

    - hosts: localhost
      roles:
       - { role: tls-create-ca, DOMAIN_NAME: local.atmo.cloud }

https://cyverse.org
