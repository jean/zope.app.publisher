##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Functional tests for xmlrpc

$Id$
"""
import sys

# Evil hack to make pickling work with classes defined in doc tests
class NoCopyDict(dict):
    def copy(self):
        return self

class FakeModule:
    def __init__(self, dict):
        self.__dict = dict
    def __getattr__(self, name):
        try:
            return self.__dict[name]
        except KeyError:
            raise AttributeError, name

globs = NoCopyDict()
name = 'zope.app.publisher.xmlrpc.README'


def setUp():
    globs['__name__'] = name    
    sys.modules[name] = FakeModule(globs)

def tearDown():
    globs.clear()
    del sys.modules[name]

def test_suite():
    from zope.app.tests.functional import FunctionalDocFileSuite
    return FunctionalDocFileSuite(
        'README.txt',
        setUp=setUp, tearDown=tearDown, globs=globs)

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='test_suite')
