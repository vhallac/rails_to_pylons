from sample_app.tests import *
from sample_app.lib.base import render
from mock import patch

class TestLinks(TestIntegration):

    @patch("sample_app.controllers.pages.render")
    def test_templates(self, mock):
        tests = [
            { "url": "/",        "template": "/derived/pages/home.mako"},
            { "url": "/contact", "template": "/derived/pages/contact.mako"},
            { "url": "/about",   "template": "/derived/pages/about.mako"},
            { "url": "/help",    "template": "/derived/pages/help.mako"},
            ]
        mock.return_value = ""
        for i in tests:
            r = self.app.get(i["url"])
            mock.assert_called_with(i["template"])

    @patch("sample_app.controllers.pages.render")
    @patch("sample_app.controllers.users.render")
    def test_links(self, users_mock, pages_mock):
        pages_mock.side_effect = render
        users_mock.side_effect = render
        r = self.app.get("/")
        r = r.click("About")
        assert r.request.path_qs == "/about"
        pages_mock.assert_called_with("/derived/pages/about.mako")
        r = r.click("Help")
        assert r.request.path_qs == "/help"
        pages_mock.assert_called_with("/derived/pages/help.mako")
        r = r.click("Contact")
        assert r.request.path_qs == "/contact"
        pages_mock.assert_called_with("/derived/pages/contact.mako")
        r = r.click("Home")
        assert r.request.path_qs == "/"
        pages_mock.assert_called_with("/derived/pages/home.mako")
        r = r.click("Sign up now")
        assert r.request.path_qs == "/signup"
        users_mock.assert_called_with("/derived/users/new.mako")
