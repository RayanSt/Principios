import abc
from abc import ABCMeta


#class Coche():
#    __marca = ""
#
#    def __init__(self,marca):
#        self.__marca = marca
#
#    def getMarca(self):
#        return  self.__marca





class CocheBD(object):
    nombre = ""
    def GuardarDato(self, nombre):
        self.nombre = nombre



    def EliminarDato(self):
        self.nombre = ""



class Coche(object):
    __metaclass__ = ABCMeta
    @abc.abstractmethod
    def precioMedioCoche(self):
        pass


class Renault(Coche):
    def precioMedioCoche(self):
        return 18000


class Audi (Coche):
    def precioMedioCoche(self):
        return 25000


class Mercedes(Coche):
    def precioMedioCoche(self):
        return 27000

def imprimirPrecioMedioCoche(arrayCoches):
        print(str(arrayCoches.precioMedioCoche()))

arrayCoches = [ Renault(), Audi(), Mercedes() ]
print(Renault.precioMedioCoche())
#imprimirPrecioMedioCoche(arrayCoches);




