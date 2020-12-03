from abc import ABC, abstractmethod
import requests
import json

class Pelicula():

    def __init__(self,id,titulo,genero,fecha_lanz,poster,rating,sinopsis,trailer=None,relacionados=None,link=None):

        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.fecha_lanz = fecha_lanz
        self.poster = poster
        self.rating = rating
        self.sinopsis = sinopsis
        self.trailer = trailer
        self.relacionados = relacionados
        self.link = link




class AbstractApi(ABC):    #interfaceAPI
    @abstractmethod
    def get_pelicula(self, nombre):
        pass
        """Toma como parametro el nombre de la película y regresa un objeto de tipo película, la clase que se que conecte al api
        implementa esta clase abstracta"""

class AbstractDb(ABC):   #InterfaceBD
    @abstractmethod
    def crearTablaPeliculas(self):
        pass

    @abstractmethod
    def insertarPelicula(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula (obtenido siempre del metodo get_pelicula),
        y regresa la consulta de la pelicula con sus datos, la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def agregarTrailer(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula, actualiza en la BD y regresa una consulta con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""


    @abstractmethod
    def agregarRelacionados(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula, actualiza en la BD y regresa una consulta con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def agregarLink(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula, actualiza en la BD y regresa una consulta con los nuevos datos,
        la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def consultarPelicula(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula y regresa una consulta con sus datos,
        la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def eliminarPelicula(self, pelicula):
        pass
        """Toma como parametro un objeto de tipo pelicula, la elimina en la BD y regresa una consulta para verificar
        que se eliminó, la clase que se conecta a la base de datos implementa este metodo"""

    @abstractmethod
    def get_pelicula(self, titulo):
        pass
        """Toma como parametro el titulo de una pelicula, hace su consulta en la BD y crea un objeto Pelicula con esos datos,
        la clase que se conecta a la base de datos implementa este metodo"""


