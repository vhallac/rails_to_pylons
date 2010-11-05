from sample_app.tests import *
from mock import Mock, patch
from sample_app.tests.factories import UserFactory
import re

class TestUsersController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='users', action='new'))
        assert have_tag(response, "title", "Sign up")

    @classmethod
    def setupClass(cls):
        cls.clean_db()
        cls.user = UserFactory.create()
        cls.queryMock = Mock()

    @patch("sample_app.controllers.users.render")
    def test_templates(self, mock):
        tests = [
            { "url": "/signup", "template": "/derived/users/new.mako"},
            ]
        mock.return_value = ""
        for i in tests:
            r = self.app.get(i["url"])
            mock.assert_called_with(i["template"])

    def test_show(self):
        self.app.get(url(controller='users', action='show', id=self.user.id))

    def test_title(self):
        response = self.app.get(url(controller='users', action='show', id=self.user.id))
        assert have_tag(response, "title", self.user.name)

    def test_heading(self):
        response = self.app.get(url(controller='users', action='show', id=self.user.id))
        assert have_tag(response, "h2", self.user.name)

    def test_profile_image(self):
        response = self.app.get(url(controller='users', action='show', id=self.user.id))
        # The test from the tutorial is for h2>img, but I don't want to extend
        # the have_tag too much for now. A possibility is to use soupselect from
        # http://code.google.com/p/soupselect/ which allows for CSS-like
        # selectors.
        # For now, checking for the img tag should be enough
        assert have_tag(response, "img", attrs={"class": "gravatar"})
