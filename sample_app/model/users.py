from meta import Base
import sqlalchemy as sa
from sqlalchemy.orm import mapper, validates, synonym
from datetime import datetime

users_table = sa.Table('users', Base.metadata,
                       sa.Column('id', sa.Integer,
                                 sa.Sequence('user_id_seq'), primary_key=True),
                       sa.Column('name', sa.String, nullable=False),
                       sa.Column('email', sa.String, index=True, unique=True),
                       sa.Column('created_at', sa.DateTime, default=datetime.now),
                       sa.Column('updated_at', sa.DateTime,
                                 onupdate=datetime.now,
                                 default=datetime.now),
                       )

def readonly_property(real_name):
    return property(lambda(obj): obj.__getattribute__(real_name))

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

    created_at = readonly_property("_created_at")
    updated_at = readonly_property("_updated_at")

    def set_created_at(self, val):
        pass

    def set_created_at(self, val):
        pass

    def __repr__(self):
        return "<User(name='%s', email='%s')>"%(self.name, self.email)

# Map the object to the database table
mapper(User, users_table,
       properties = {
        'created_at': synonym('_created_at', map_column=True),
        'updated_at': synonym('_updated_at', map_column=True),
        },
)
