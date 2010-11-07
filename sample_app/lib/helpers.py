"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import *
from webhelpers.pylonslib.flash import Flash as _Flash
from pylons import url
import gravatar
from pylons import tmpl_context as c

flash = _Flash()

def title():
    base_title = "Ruby on Rails Tutorial Sample App"
    if "title" not in dir(c) or c.title is None:
        return base_title
    else:
        return "%s | %s"%(base_title, c.title)

def gravatar_img(email):
    return image(gravatar.make(email), "gravatar", class_="gravatar")
