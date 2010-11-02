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

from mock import Mock, patch

import pylons.test

__all__ = ['environ', 'url', 'TestController', 'have_tag']

# Invoke websetup with the current config file
SetupCommand('setup-app').run([pylons.test.pylonsapp.config['__file__']])

environ = {}

class TestController(TestCase):

    def __init__(self, *args, **kwargs):
        wsgiapp = pylons.test.pylonsapp
        config = wsgiapp.config
        self.app = TestApp(wsgiapp)
        url._push_object(URLGenerator(config['routes.map'], environ))
        TestCase.__init__(self, *args, **kwargs)

    def make_template_checker(self, controller, url, template):
        """Make a function that will load the specified URL, and check if it
        renders the given URL.

        Arguments:
        - `controller`: The module name of the controller that contains the
          'render' function.
        - `url`: The url to check
        - `template`: The template file that should be rendered. It is relative
          to the tempates directory (e.g. /derived/pages/home.mako)
        """

        @patch("sample_app.controllers."+controller+".render")
        def test_func(self, mock):
            mock.return_value = ""
            r = self.app.get(url)
            mock.assert_called_with(template)

        return test_func

import re

def have_tag(response, tag, content):
    elt = response.html.find(tag)
    return elt is not None and re.compile(content).search(elt.encodeContents())
