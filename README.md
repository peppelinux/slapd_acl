# slapd_acl
slapd olcAccess (ACLs) utility

Your olcAccess in a human readable way.

#### Requirements
ldapsearch

#### Setup
````
pip3 install slapd_acl
````

#### Usage
using ldapi and mdb (default behaviour)
````
slapd_acl
````

using different paramenters
````
usage: slapd_acl [-h] [-H H] [-Y Y] [-D D] [-w W] [-b B] [-ldif] [-enc ENC]

optional arguments:
  -h, --help  show this help message and exit
  -H H        Base LDAP Search
  -Y Y        SASL mechanism
  -D D        example cn:admin,dc=example,dc=org
  -w W        the user password
  -b B        Base LDAP Search
  -ldif       print a modify ldif
  -enc ENC    encoding
````

#### Modify ldif
`-ldif` option make the output in a ldif modify format. 

#### Authors
Giuseppe De Marco
