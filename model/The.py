from google.appengine.ext import ndb


class The(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    descripcion = ndb.TextProperty()
    tipo = ndb.StringProperty()
    tiempoInfusion = ndb.StringProperty()
    temperatura = ndb.StringProperty()
    gramos = ndb.StringProperty()
    identificateur = ndb.StringProperty()
    likes = ndb.StringProperty(indexed=True)
