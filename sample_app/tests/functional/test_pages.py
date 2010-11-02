from sample_app.tests import *
from mock import patch

from sample_app.lib.base import render

class TestPagesController(TestController):
    # A little constant to reduce repetition in the test cases below
    title_prefix = "Ruby on Rails Tutorial Sample App | "

    def test_home(self):
        response = self.app.get(url(controller='pages', action='home'))
        assert have_tag(response, "title", self.title_prefix+"Home")

    def test_contact(self):
        response = self.app.get(url(controller='pages', action='contact'))
        assert have_tag(response, "title", self.title_prefix+"Contact")

    def test_about(self):
        response = self.app.get(url(controller='pages', action='about'))
        assert have_tag(response, "title", self.title_prefix+"About")

    def test_about(self):
        response = self.app.get(url(controller='pages', action='help'))
        assert have_tag(response, "title", self.title_prefix+"Help")
