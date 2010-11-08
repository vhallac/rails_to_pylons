from sample_app.tests import *
from sample_app.lib.base import render
from sample_app.model import Session, User
from mock import patch

class TestUser_Signup(TestSite):
    @classmethod
    def setUpClass(cls):
        cls.clean_db()

    @patch("sample_app.controllers.users.render")
    def test_empty_form(self, mock):
        mock.side_effect = render
        response = self.app.get(url('/users/new'))
        assert response.form is not None
        response = response.form.submit('submit')
        mock.assert_called_with('/derived/users/new.mako')
        assert have_tag(response, 'input', attrs = {"id": "name",
                                                    "class": "error"})
        assert have_tag(response, 'input', attrs = {"id": "email",
                                                    "class": "error"})
        assert have_tag(response, 'input', attrs = {"id": "password",
                                                    "class": "error"})

    def test_no_new_user(self):
        start_count = Session.query(User).count()
        response = self.app.get(url('/users/new'))
        response = response.form.submit('submit')
        assert start_count == Session.query(User).count()

    @patch("sample_app.controllers.users.render")
    def test_new_user(self, mock):
        mock.side_effect = render
        start_count = Session.query(User).count()
        response = self.app.get(url('/users/new'))
        assert response.form is not None
        response.form["name"] = "Example User"
        response.form["email"] = "user@example.com"
        response.form["password"] = "foobar"
        response.form["password_confirmation"] = "foobar"
        response = response.form.submit('submit')
        assert response.status_int == 302
        response = response.follow()
        mock.assert_called_with("/derived/users/show.mako")
        assert start_count + 1 == Session.query(User).count()
