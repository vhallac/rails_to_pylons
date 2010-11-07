import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from pylons.decorators import validate
import sample_app.model as model
import formencode
from formencode import htmlfill
from sqlalchemy.exc import DatabaseError

from sample_app.lib.base import BaseController, render
from sample_app.lib import local_validators

log = logging.getLogger(__name__)

# TODO: Feature missing (compared to Rails) - authenticiy token, for forgery
# attacks. Read more about it.
class SignupForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty = True, max = 50)
    password = formencode.validators.String(min = 6, max = 40)
    password_confirmation = formencode.validators.String() # No additional constaints for this. Gotta be equal to password anyway.
    email = formencode.All(formencode.validators.Email(not_empty = True),
                           local_validators.Unique(orm_class = model.User, filter_column='email'))
    chained_validators = [
        formencode.validators.FieldsMatch('password', 'password_confirmation'),
        ]


class UsersController(BaseController):

    def new(self):
        c.title = "Sign up"
        return render('/derived/users/new.mako')

    # TODO: Any way to enclose error message and field inside a <div>?
    @validate(schema=SignupForm, form="new")
    def create(self):
        try:
            user = model.User(self.form_result["name"],
                              self.form_result["email"],
                              self.form_result["password"])
            model.Session.add(user)
            model.Session.commit()
            response.status_int = 302
            response.headers['location'] = url('user', id=user.id)
        except DatabaseError, e:
            # TODO: How should we handle this? The only exceptions I can think
            # of are broken DB operations, now that we handle unique e-mails in
            # the form validator. Maybe display an error page?
            return self.new()

    def show(self, id, format='html'):
        c.user = model.Session.query(model.User).filter(model.User.id == id).first()
        c.title = c.user.name
        return render('/derived/users/show.mako')
