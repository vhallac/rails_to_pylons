"""Pylons application test package

This package assumes the Pylons environment is already loaded, such as
when this script is imported from the `nosetests --with-pylons=test.ini`
command.

This module initializes the application via ``websetup`` (`paster
setup-app`) and provides the base testing objects.
"""
from unittest import TestCase

from paste.deploy import loadapp
from paste.script.appinstall import SetupCommand
from pylons import url
from routes.util import URLGenerator
from webtest import TestApp
from sample_app.model import Session
from sample_app.model.meta import Base

import pylons.test

__all__ = ['environ', 'url', 'TestController', 'TestSite', 'TestModel', 'have_tag']

# Invoke websetup with the current config file
SetupCommand('setup-app').run([pylons.test.pylonsapp.config['__file__']])

environ = {}

class WebTest(TestCase):

    def __init__(self, *args, **kwargs):
        wsgiapp = pylons.test.pylonsapp
        config = wsgiapp.config
        url._push_object(URLGenerator(config['routes.map'], environ))
        self.app = TestApp(wsgiapp)
        TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def clean_db(self):
        Base.metadata.drop_all(bind=Session.bind)
        Base.metadata.create_all(bind=Session.bind)

class TestController(WebTest):
    pass

class TestSite(WebTest):
    pass

class TestModel(WebTest):
    pass

import re

def have_tag(response, tag, content):
    elt = response.html.find(tag)
    return elt is not None and re.compile(content).search(elt.encodeContents())
