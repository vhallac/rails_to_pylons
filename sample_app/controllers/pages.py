import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sample_app.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def home(self):
        return render("/derived/pages/home.mako")

    def contact(self):
        return render('/derived/pages/contact.mako')
