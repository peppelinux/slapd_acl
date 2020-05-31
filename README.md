# slapd acl
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

#### Example
````
root@ldapmaster:~# slapd_acl -ldif
Executing:
 ldapsearch -Y EXTERNAL -H ldapi:///  -b 'olcDatabase={1}mdb,cn=config' -s base 'olcAccess' -LLL

SASL/EXTERNAL authentication started
SASL username: gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth
SASL SSF: 0

dn: olcDatabase=olcDatabase={1}mdb,cn=config
changeType: modify
replace: olcAccess
{0}to *  
 by dn.exact=gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth manage  
 by * break 
{1}to attrs=userPassword,shadowLastChange,mail  
 by self write  
 by anonymous auth  
 by * break 
{2}to *  
 by dn.children="ou=repl,dc=testunical,dc=it" read  
 by * break 
{3}to dn.subtree="ou=people,dc=testunical,dc=it"  
 by dn.children="ou=idp,dc=testunical,dc=it" read  
 by self read  
 by * break 
{4}to *  
 by anonymous auth  
 by * break 
````

#### Authors
Giuseppe De Marco
