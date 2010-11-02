import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sample_app.lib.base import BaseController, render

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def new(self):
        c.title = "Sign up"
        return render('/derived/users/new.mako')
