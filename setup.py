from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Download\n'
    '********\n'
    )

open('doc.txt', 'w').write(long_description)

setup(
    name='grok',
    version='0.10',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='http://grok.zope.org',
    download_url='http://cheeseshop.python.org/pypi/grok/',
    description='Grok: Now even cavemen can use Zope 3!',
    long_description=long_description,
    license='ZPL',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    install_requires=['setuptools',
                      'martian',
                      'simplejson',
                      'pytz',
                      'ZODB3 == 3.8.0b2',
                      'zope.annotation',
                      'zope.app.apidoc',
                      'zope.app.applicationcontrol',
                      'zope.app.appsetup',
                      'zope.app.authentication',
                      'zope.app.catalog',
                      'zope.app.component',
                      'zope.app.container == 3.5.0.a1',
                      'zope.app.folder',
                      'zope.app.intid',
                      # not binary, but needed for ZODB 3.8.0b2
                      'zope.app.keyreference == 3.4.0a1',
                      'zope.app.pagetemplate',
                      'zope.app.publication',
                      'zope.app.publisher',
                      'zope.app.renderer',
                      'zope.app.security',
                      'zope.app.securitypolicy',
                      'zope.app.testing',
                      'zope.app.twisted',
                      'zope.app.zcmlfiles',
                      'zope.component',
                      'zope.configuration',
                      'zope.dottedname',
                      'zope.deprecation',
                      'zope.event',
                      'zope.formlib',
                      'zope.hookable',
                      'zope.i18nmessageid',
                      'zope.interface == 3.4.0',
                      'zope.lifecycleevent',
                      'zope.pagetemplate',
                      'zope.proxy == 3.4.0',
                      'zope.publisher',
                      'zope.schema',
                      'zope.security == 3.4.0b5',
                      'zope.testing',
                      'zope.traversing',
                      'zope.testbrowser',
                      'zc.catalog',
                      'z3c.flashmessage >=1.0b1',
                      ],
)
