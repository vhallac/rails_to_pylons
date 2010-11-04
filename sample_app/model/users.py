from meta import Base
import sqlalchemy as sa
from sqlalchemy.orm import mapper, validates

users_table = sa.Table('users', Base.metadata,
                       sa.Column('id', sa.Integer,
                                 sa.Sequence('user_id_seq'), primary_key=True),
                       sa.Column('name', sa.String, nullable=False),
                       sa.Column('email', sa.String, index=True, unique=True),
                       )

class User(object):
    def __init__(self, name="", email=""):
        self.valid = True
        self.name = name
        self.email = email

    # Experimental code for handling validations at model level. Leaving it in
    # for future work - if I get around to coming back to Chapter 6 of the
    # tutorial.
    @validates('name')
    def validate_name(self, key, value):
        if value is None or len(value) == 0:
            self.valid = False
        return value

    def __repr__(self):
        return "<User(name='%s', email='%s')>"%(self.name, self.email)

# Map the object to the database table
mapper(User, users_table)
