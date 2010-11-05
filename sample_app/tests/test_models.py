from sample_app.tests import *
from sample_app.model.meta import Session
from sample_app import model

from sqlalchemy import engine_from_config

class TestUserModel(TestModel):
    a_user = { "name"     : "vedat",
               "email"    : "vedat@example.com",
               "password" : "password" }

    @classmethod
    def setUpClass(self):
        self.clean_db()
        self.user = model.User(**self.a_user)
        Session.add(self.user)
        Session.commit()

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
