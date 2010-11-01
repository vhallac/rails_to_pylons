#TODO: Is this overkill?
from BeautifulSoup import BeautifulSoup
from sample_app.tests import *

def have_tag(response, tag, content):
    soup = BeautifulSoup(response.body)
    elt = soup.find(tag)
    return elt is not None and elt.encodeContents() == content

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
