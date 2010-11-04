import meta
import sqlalchemy as sa
from sqlalchemy.orm import mapper, validates, synonym
from datetime import datetime
from hashlib import sha256

users_table = sa.Table('users', meta.Base.metadata,
                       sa.Column('id', sa.Integer,
                                 sa.Sequence('user_id_seq'), primary_key=True),
                       sa.Column('name', sa.String, nullable=False),
                       sa.Column('email', sa.String, index=True, unique=True),
                       sa.Column('salt', sa.String),
                       sa.Column('encrypted_password', sa.String),
                       sa.Column('created_at', sa.DateTime, default=datetime.now),
                       sa.Column('updated_at', sa.DateTime,
                                 onupdate=datetime.now,
                                 default=datetime.now),
                       )

def readonly_property(real_name):
    return property(lambda(obj): obj.__getattribute__(real_name))

class User(object):
    def __init__(self, name="", email="", password=""):
        self.valid = True
        self.name = name
        self.email = email
        self.password = password

    def has_password(self, password):
        """Return true if the password of the user matches the specified password.

        Arguments:
        - `password`: The password to check against
        """
        return self.password == self._encrypt(password)

    @classmethod
    def authenticate(cls, email, password):
        user = meta.Session.query(User).filter(User.email == email).first()
        if user is not None:
            if not user.has_password(password):
                user = None
        return user

    # Experimental code for handling validations at model level. Leaving it in
    # for future work - if I get around to coming back to Chapter 6 of the
    # tutorial.
    @validates('name')
    def validate_name(self, key, value):
        if value is None or len(value) == 0:
            self.valid = False
        return value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self.salt = self._make_salt()
        self._password = self._encrypt(password)

    created_at = readonly_property("_created_at")
    updated_at = readonly_property("_updated_at")

    # Not really encrypting anything, but let's stay tru to tutorial. :)
    def _encrypt(self, password):
        return self._secure_hash("%s%s"%(self.salt, password))

    def _make_salt(self):
        return self._secure_hash("%s%s"%(str(datetime.utcnow()),self.email))

    def _secure_hash(self, string):
        return sha256(string).hexdigest()

    def __repr__(self):
        return "<User(name='%s', email='%s')>"%(self.name, self.email)

# Map the object to the database table
mapper(User, users_table,
       properties = {
        'created_at': synonym('_created_at', map_column=True),
        'updated_at': synonym('_updated_at', map_column=True),
        'encrypted_password': synonym('_password', map_column=True),
        },
)
