import factory
from sample_app.model import Session
from sample_app.model.users import User

def create_obj(cls, **kwargs):
    obj = cls(**kwargs)
    Session.add(obj)
    Session.commit()
    return obj

factory.Factory.set_creation_function(create_obj)

class UserFactory(factory.Factory):
    name = "Vedat Hallac"
    email = "vhallac@example.com"
    password = "foobar"
