"""The application's model objects"""
from sqlalchemy import orm
from meta import Session

from sample_app.model.users import User

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""

    sm = orm.sessionmaker(autoflush = True, autocommit = False, bind = engine)

    meta.engine = engine
    meta.Session = orm.scoped_session(sm)
    Session.configure(bind = engine)
