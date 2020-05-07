#!/usr/bin/env python
import jinja2 as jinja2
import webapp2
from webapp2_extras import jinja2
from model.The import The
from webapp2_extras.users import users


class MainHandler(webapp2.RequestHandler):
    def post(self):
        usr = users.get_current_user()
        if usr:
            usr_url = users.create_logout_url("/")
            nom = self.request.get("nom")
            description = self.request.get("description")
            tipe = self.request.get("tipe")
            duration = self.request.get("duration")
            temperature = self.request.get("tempe")
            grames = self.request.get("grames")
            origen = self.request.get("origen")
            id = int(int(The.query().order(-The.likes).count()) + 1)
            like = int(self.request.get("likes"))
            use = str("")
            the = The(nombre=nom, descripcion=description, tipo=tipe, tiempoInfusion=duration,
                      temperatura=temperature, gramos=grames, identificateur=id, likes=like, origen=origen, users=use)
            the.put()
        else:
            usr_url = users.create_login_url("/")
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes,
            "usr": usr,
            "usr_url": usr_url
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class GetHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if usr:
            usr_url = users.create_logout_url("/")
        else:
            usr_url = users.create_login_url("/")
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes,
            "usr": usr,
            "usr_url": usr_url
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


class HomeHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if usr:
            usr_url = users.create_logout_url("/")
        else:
            usr_url = users.create_login_url("/")
        thes = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes,
            "usr": usr,
            "usr_url": usr_url
        }
        self.response.write(jinja.render_template("main.html", **valeurs))


class JaimeHandler(webapp2.RequestHandler):
    def post(self):
        usr = users.get_current_user()
        if usr:
            usr_url = users.create_logout_url("/")
            id = self.request.get("identifi")
            thes = The.query().order(-The.likes)
            if thes.count() != 0:
                for data in thes:
                    if str(data.identificateur) == str(id):
                        usrs = str(data.users).split()
                        print(usr)
                        if str(usr) not in usrs:
                            data.likes = int(int(data.likes) + 1)
                            data.users += str(str(usr) + " ")
                            data.put()
        else:
            usr_url = users.create_login_url("/")
        thes_actualise = The.query().order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes_actualise,
            "usr": usr,
            "usr_url": usr_url
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


class RechercheHandler(webapp2.RequestHandler):
    def post(self):
        usr = users.get_current_user()
        if usr:
            usr_url = users.create_logout_url("/")
        else:
            usr_url = users.create_login_url("/")
        nom = str(self.request.get("nomT"))
        if nom == "tout":
            thes = The.query().order(-The.likes)
        else:
            thes = The.query(The.tipo == nom).order(-The.likes)
        jinja = jinja2.get_jinja2(app=self.app)
        valeurs = {
            "datas": thes,
            "usr": usr,
            "usr_url": usr_url
        }
        self.response.write(jinja.render_template("reponse.html", **valeurs))


app = webapp2.WSGIApplication([('/home', HomeHandler),
                               ('/montrer', GetHandler),
                               ('/ajouter?', MainHandler),
                               ('/gusta?', JaimeHandler),
                               ('/recherche?', RechercheHandler)], debug=True)
