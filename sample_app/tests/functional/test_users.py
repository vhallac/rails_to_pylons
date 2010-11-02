from sample_app.tests import *
from mock import patch
import re

class TestUsersController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='users', action='new'))
        assert have_tag(response, "title", "Sign up")

    @patch("sample_app.controllers.users.render")
    def test_templates(self, mock):
        tests = [
            { "url": "/signup", "template": "/derived/users/new.mako"},
            ]
        mock.return_value = ""
        for i in tests:
            r = self.app.get(i["url"])
            mock.assert_called_with(i["template"])
