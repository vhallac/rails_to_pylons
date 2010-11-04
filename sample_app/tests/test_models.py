import pylons.test
from unittest import TestCase
from webtest import TestApp

from sample_app.model import init_model
from sample_app.model.meta import Base, Session
from sample_app import model

from sqlalchemy import create_engine

def setup():
    pass
    # To create tables, you typically do:
    #    model.metadata.create_all(engine)

def teardown():
    Session.remove() # Is this applicable?


class TestUserModel(TestCase):
    a_user = { "name"     : "vedat",
               "email"    : "vedat@example.com",
               "password" : "password" }

    # Move to __init__ along with the above definitions?
    def __init__(self, *args, **kwargs):
        wsgiapp = pylons.test.pylonsapp
        self.app = TestApp(wsgiapp)
        TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(self):
        self.user = model.User(**self.a_user)
        Session.add(self.user)
        Session.commit()

    @classmethod
    def tearDownClass(self):
        pass

    def test_columns(self):
        columns = ['name', 'email', 'password']
        for col in columns:
            assert col in dir(self.user)

    def test_find(self):
        user = Session.query(model.User).filter(model.User.email == self.a_user["email"]).first()
        assert user == self.user

    def test_valid_password(self):
        assert self.user.has_password(self.a_user["password"])

    def test_invalid_password(self):
        assert not self.user.has_password("invalid")

    def test_auth_bad_password(self):
        user = model.User.authenticate(self.a_user["email"], "incorrect")
        assert user is None

    def test_auth_bad_email(self):
        user = model.User.authenticate("wrong@email.com", self.a_user["password"])
        assert user is None

    def test_auth_match(self):
        user = model.User.authenticate(self.a_user["email"], self.a_user["password"])
        assert user == self.user
