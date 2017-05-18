tls-ca-sign-csr
=========

Sign a certificate signing request with a certificate authority

The intention is that this playbook will **not** be used in production. It is
useful for local development but is otherwise a major liability.

Role Variables
--------------

It accepts a CA certificate, ca key, and certificate request, and signs the request as the
CA. It generates TLS_SIGNED_CERT_DEST. See example playbook below.

| Variable                     | Required        | Default             | Choices | Comment                       |
|------------------------------|-----------------|---------------------|---------|-------------------------------|
| TLS_CA_CERT_DEST             | yes             |                     |         | Path to ca cert               |
| TLS_CA_KEY_DEST              | yes             |                     |         | Path to ca key                |
| TLS_CERT_REQUEST_DEST        | yes             |                     |         | Path to cert signing request  |
| TLS_SIGNED_CERT_DEST         | no              | server_cert.pem     |         | Path to generated signed cert |

Example Playbook
----------------

    - hosts: localhost
      roles:
       - { role: tls-ca-sign-csr,
           TLS_CA_CERT_DEST: ./ca_cert.pem,
           TLS_CA_KEY_DEST: ./ca_cert_key.pem,
           TLS_CERT_REQUEST_DEST: ./server_cert_csr.pem }

https://cyverse.org
