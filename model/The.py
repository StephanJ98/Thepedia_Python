from google.appengine.ext import ndb


class The(ndb.Model):
    nombre = ndb.StringProperty(indexed=True)
    descripcion = ndb.TextProperty()
    tipo = ndb.StringProperty()
    tiempoInfusion = ndb.StringProperty()
    temperatura = ndb.StringProperty()
    origen = ndb.StringProperty()
    gramos = ndb.StringProperty()
    identificateur = ndb.IntegerProperty()
    likes = ndb.IntegerProperty(indexed=True)
