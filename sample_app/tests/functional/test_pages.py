#TODO: Is this overkill?
from BeautifulSoup import BeautifulSoup
from sample_app.tests import *

def have_tag(response, tag, content):
    soup = BeautifulSoup(response.body)
    elt = soup.find(tag)
    return elt is not None and elt.encodeContents() == content

class TestPagesController(TestController):

    def test_home(self):
        response = self.app.get(url(controller='pages', action='home'))
        assert have_tag(response, "title", "Ruby on Rails Tutorial Sample App | Home")

    def test_contact(self):
        response = self.app.get(url(controller='pages', action='contact'))
        assert have_tag(response, "title", "Ruby on Rails Tutorial Sample App | Contact")

    def test_about(self):
        response = self.app.get(url(controller='pages', action='about'))
        assert have_tag(response, "title", "Ruby on Rails Tutorial Sample App | About")
