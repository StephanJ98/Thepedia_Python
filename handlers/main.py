#!/usr/bin/env python
import jinja2 as jinja2
import webapp2
from webapp2_extras import jinja2
from model.The import The


class MainHandler(webapp2.RequestHandler):
    def post(self):
        nom = self.request.get("nom")
        description = self.request.get("description")
        tipe = self.request.get("tipe")
        duration = self.request.get("duration")
        temperature = self.request.get("tempe")
        grames = self.request.get("grames")
        origen = self.request.get("origen")
        id = int(int(The.query().order(-The.likes).count()) + 1)
        like = int(self.request.get("likes"))
        the = The(nombre=nom, descripcion=description, tipo=tipe, tiempoInfusion=duration,
                  temperatura=temperature, gramos=grames, identificateur=id, likes=like, origen=origen)
        the.put()
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class GetHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class TheHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class JaimeHandler(webapp2.RequestHandler):
    def post(self):
        id = self.request.get("identifi")
        thes = The.query().order(-The.likes)
        if thes.count() != 0:
            for data in thes:
                if str(data.identificateur) == str(id):
                    data.likes = int(int(data.likes) + 1)
                    data.put()
        thesActualise = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thesActualise
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


app = webapp2.WSGIApplication([('/ajouter?', MainHandler),
                               ('/montrer', GetHandler),
                               ('/home', HomeHandler),
                               ('/gusta?', JaimeHandler)], debug=True)
