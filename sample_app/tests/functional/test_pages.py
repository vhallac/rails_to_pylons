from sample_app.tests import *

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

    def test_templates(self):
        tests = [
            { "url": "/",              "template": "/derived/pages/home.mako"},
            { "url": "/contact", "template": "/derived/pages/contact.mako"},
            { "url": "/about",   "template": "/derived/pages/about.mako"},
            { "url": "/help",    "template": "/derived/pages/help.mako"},
            ]
        for i in tests:
            f = self.make_template_checker("pages", i["url"], i["template"])
            f(self)
