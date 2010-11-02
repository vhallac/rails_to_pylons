"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import stylesheet_link, image, link_to
from pylons import url

from pylons import tmpl_context as c

def title():
    base_title = "Ruby on Rails Tutorial Sample App"
    if c.title is None:
        return base_title
    else:
        return "%s | %s"%(base_title, c.title)
