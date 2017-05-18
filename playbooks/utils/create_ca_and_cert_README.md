# create_ca_and_cert.yml
This is a utility playbook to create a certificate authority (CA) and
certificates signed by said authority.
See the background section below for an overview.

Steps to perform:
1. Create a CA and signed guest cert
2. Install guest cert and key on guest machine
3. Install CA cert on host machine
4. Delete all traces of your CA private key **(DO NOT SKIP!)**

## Create a CA and signed guest cert

```bash
clank.py --playbook playbooks/utils/create_ca_and_cert.yml -e /path/to/variables.yml
```
After running that playbook you should see a bunch of new `*.pem` files.

## Install guest cert and key on guest machine

Add/update the following variables in your variables file:
```yaml
TLS_PRIVKEY_SRC_FILE: "/path/to/*.server.key.pem"
TLS_CERT_SRC_FILE:    "/path/to/*.server.cert.pem"
TLS_CACHAIN_SRC_FILE: "/path/to/*.ca.cert.pem"
```

At this point you should do a redeploy.

If you want to quickly verify the certs were installed run:
```bash
# Check that private key and cert indeed match
nginx -t
```

## Install CA cert on host machine

### Firefox
If you're on Firefox you need to upload your certificate authority cert
(`/path/to/*.ca.cert.pem`) into Firefox and restart Firefox.

As of now you can navigate to preferences/advanced/certificates. You can then
select "View Certificates" and then you can navigate to "Authorities" then
click "import" and upload your certificate authority cert.

Restart Firefox.

### Chrome
On OSX, Chrome looks up your certificates using OSX Keychain Acess. You will need to
add it your keychain, manually trust it, then restart Chrome.

Prompt dialog to import your CA
```bash
open /path/to/*.ca.cert.pem
```

This should add your CA to your system keychain. Now you must double click it
in Keychain Access to manually trust it.

Click the 'trust' dropdown then set "When using this certificate: Always Trust".
When you close the window, it will prompt for your system credentials, then you
should see the certificate icon momentarily change from being red to a light
blue.

Restart Chrome.


## Delete your CA private key

If anyone gets a hold of your certificate authority private key, they can
impersonate any site and your browser will accept that fake site. I highly
suggest that you delete this private key. You won't be able to issue further
certificates but that is okay for your development environment, you can always
create a new CA.

Delete your Certificate Authority key:
```bash
rm /path/to/*.ca.key.pem

```

## Background for this approach
When you visit a site, that site first sends the browser a certificate (stamp
of approval) to prove its legitimacy.

Your browser looks at the certificate and looks at who issued/signed the
certificate. If the browser trusts the issuer, then it trusts the original
site.

One approach to setting up HTTPS for a development site is to become your own
issuer (i.e Certificate Authority), sign the certificates that your
development site will use, and lastly trust that issuer in your browser.
