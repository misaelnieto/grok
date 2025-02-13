"""
Multiple calls of grok.require in one class are not allowed.

  >>> grok.testing.grok(__name__)
  Traceback (most recent call last):
     ...
  martian.error.GrokError: grok.require was called multiple times in <class 'grok.tests.xmlrpc.multiple_require.MultipleXMLRPC'>. It may only be set once for a class.
"""  # noqa: E501
import zope.interface

import grok


class One(grok.Permission):
    grok.name('permission.1')


class Two(grok.Permission):
    grok.name('permission.2')


class MultipleXMLRPC(grok.XMLRPC):
    grok.context(zope.interface.Interface)
    grok.require(One)
    grok.require(Two)

    def render(self):
        pass
