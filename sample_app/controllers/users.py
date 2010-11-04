import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
import sample_app.model as model

from sample_app.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def new(self):
        c.title = "Sign up"
        return render('/derived/users/new.mako')

    def show(self, id, format='html'):
        c.user = model.Session.query(model.User).filter(model.User.id == id).first()
        return render('/derived/users/show.mako')
