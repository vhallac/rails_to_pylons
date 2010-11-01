import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from sample_app.lib.base import BaseController, render

log = logging.getLogger(__name__)

class PagesController(BaseController):

    def home(self):
        c.title = "Home"
        return render("/derived/pages/home.mako")

    def contact(self):
        c.title = "Contact"
        return render("/derived/pages/contact.mako")

    def about(self):
        c.title = "About"
        return render("/derived/pages/about.mako")
