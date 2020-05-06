#!/usr/bin/env python
import jinja2 as jinja2
import webapp2
from webapp2_extras import jinja2


class IndexHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {}
        self.response.write(jinja.render_template("index.html", **valeurs))


app = webapp2.WSGIApplication([('/', IndexHandler)], debug=True)