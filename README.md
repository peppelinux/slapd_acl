# slapd acl
slapd olcAccess (ACLs) utility, your olcAccess in a human readable way.


#### Requirements
ldapsearch


#### Setup
````
pip3 install slapd_acl
````

#### Usage
using ldapi and mdb (default behaviour)
````
slapd_acl -Y EXTERNAL
````

specifing a base
````
slapd_acl -Y EXTERNAL -b 'olcDatabase={0}config,cn=config'
````

remote connection
````
slapd_acl -H ldap://10.0.3.200 -D "cn=admin,dc=testunical,dc=it" -w slapdsecret -ldif
````

using different paramenters
````
usage: slapd_acl [-h] [-H H] [-Y Y] [-D D] [-w W] [-b B] [-ldif] [-enc ENC]

optional arguments:
  -h, --help  show this help message and exit
  -H H        LDAP URL
  -Y Y        SASL mechanism
  -D D        example cn:admin,dc=example,dc=org
  -w W        the user password
  -b B        Base LDAP Search
  -ldif       print a modify ldif
  -enc ENC    encoding
````

#### Modify ldif
`-ldif` option make the output in a ldif modify format. 


#### Example
````
root@ldapmaster:~# slapd_acl -ldif
Executing:
 ldapsearch -Y EXTERNAL -H ldapi:///  -b 'olcDatabase={1}mdb,cn=config' -s base 'olcAccess' -LLL

SASL/EXTERNAL authentication started
SASL username: gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth
SASL SSF: 0

dn: olcDatabase={1}mdb,cn=config
changeType: modify
replace: olcAccess
olcAccess: to * 
 by dn.exact=gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth manage 
 by dn.exact="cn=admin,dc=testunical,dc=it" manage 
 by * break 
olcAccess: to attrs=userPassword,shadowLastChange,mail 
 by self write 
 by anonymous auth 
 by * break 
olcAccess: to * 
 by dn.children="ou=repl,dc=testunical,dc=it" read 
 by * break 
olcAccess: to dn.subtree="ou=people,dc=testunical,dc=it" 
 by dn.children="ou=idp,dc=testunical,dc=it" read 
 by self read 
 by * break 
olcAccess: to * 
 by anonymous auth 
 by * break 
````

#### Authors
Giuseppe De Marco
