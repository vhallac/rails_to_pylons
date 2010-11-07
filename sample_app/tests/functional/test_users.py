from sample_app.tests import *
from sample_app.model import Session, User
from mock import Mock, patch
from sample_app.tests.factories import UserFactory
import re
from urlparse import urlparse

class TestUsersController(TestController):

    @patch("sample_app.controllers.users.render")
    def test_templates(self, mock):
        tests = [
            { "url": "/signup", "template": "/derived/users/new.mako"},
            ]
        mock.return_value = ""
        for i in tests:
            r = self.app.get(i["url"])
            mock.assert_called_with(i["template"])

class TestUsersController_Show(TestController):
    @classmethod
    def setupClass(cls):
        cls.clean_db()
        cls.user = UserFactory.create()
        cls.queryMock = Mock()

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

class TestUsersController_New(TestController):
    @classmethod
    def setUpClass(cls):
        cls.clean_db()
        cls.a_baduser = dict(name="",
                             email="",
                             password="",
                             password_confirmation="")

        cls.a_user = dict(name="user",
                          email="user@example.com",
                          password="foobar",
                          password_confirmation="foobar")

    def test_presence(self):
        self.app.get(url(controller="users", action="new"))

    def test_title(self):
        response = self.app.get(url(controller='users', action='new'))
        assert have_tag(response, "title", "Sign up")

    @patch("sample_app.controllers.users.render")
    def test_failure(self, mock):
        mock.return_value = ""
        response = self.app.post(url(controller='users', action='create'), params=self.a_baduser)
        mock.assert_called_with("/derived/users/new.mako")

    def test_success(self):
        response = self.app.post(url(controller='users', action='create'), params=self.a_user)
        u=Session.query(User).filter(User.email==self.a_user["email"]).first()
        assert response.status_int == 302, response.status
        assert urlparse(response.response.location).path == url('user', id=u.id)
        assert response.session.has_key("flash")
        msg = response.session["flash"]
        assert re.search("welcome to the sample app", msg[0][1], re.I)
