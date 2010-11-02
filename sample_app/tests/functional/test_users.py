from sample_app.tests import *
import re

class TestUsersController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='users', action='new'))
        assert have_tag(response, "title", "Sign up")

    def test_templates(self):
        tests = [
            { "url": "/signup", "template": "/derived/users/new.mako"},
            ]
        for i in tests:
            f = self.make_template_checker("users", i["url"], i["template"])
            f(self)
