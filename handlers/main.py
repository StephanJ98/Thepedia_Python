#!/usr/bin/env python
import jinja2 as jinja2
import webapp2
from webapp2_extras import jinja2
from model.The import The


# Gestiona la funcionalidad de añadir un núevo te al datastore y redirige hacia la pagina principal.
class MainHandler(webapp2.RequestHandler):
    def post(self):
        nom = self.request.get("nom")
        description = self.request.get("description")
        tipe = self.request.get("tipe")
        duration = self.request.get("duration")
        temperature = self.request.get("tempe")
        grames = self.request.get("grames")
        id = self.request.get("identificateur")
        like = self.request.get("likes")
        the = The(nombre=nom, descripcion=description, tipo=tipe,
                  tiempoInfusion=duration, temperatura=temperature, gramos=grames, identificateur=id, likes=like)
        the.put()
        thes = The.query().order(The.nombre)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


# Gestiona la funcionalidad de mostrar los tes almacenados en el datastore.
class GetHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


# Gestiona la parte back-end de la redirección de la pagina de carga a la pagina principal.
class HomeHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(The.nombre)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class TheHandler(webapp2.RequestHandler):
    def get(self):
        thes = The.query().order(The.nombre)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


# Gestiona la funcionalidad de añadir un 'like' a un te.
class JaimeHandler(webapp2.RequestHandler):
    def post(self):
        id = self.request.get("identifi")
        like = self.request.get("jaime")
        thes = The.query().order(-The.likes)
        if thes.count() != 0:
            for data in thes:
                if data.identificateur == id:
                    data.likes = unicode(int(like) + 1)
                    data.put()
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


app = webapp2.WSGIApplication([('/ajouter?', MainHandler),
                               ('/montrer', GetHandler),
                               ('/home', HomeHandler),
                               ('/gusta?', JaimeHandler)], debug=True)
