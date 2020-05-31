from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='slapd_acl',
      version='0.1.0',
      description="Slapd olcAccess (ACL) utility",
      long_description=readme(),
      classifiers=['Development Status :: 5 - Production/Stable',
                  'License :: OSI Approved :: Apache Software License',
                  'Programming Language :: Python :: 3'],
      url='https://github.com/peppelinux/slapd_acl',
      author='Giuseppe De Marco',
      author_email='giuseppe.demarco@unical.it',
      license='Apache Software License',
      scripts=['slapd_acl/slap_acl'],
      packages=['slapd_acl'],
      install_requires=[],
     )
