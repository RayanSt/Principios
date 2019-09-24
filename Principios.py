import abc
from abc import ABCMeta

#sustitucion de liscov
#open/close
#reponsabilidad unica


class CocheBD(object):
    nombre = ""
    def GuardarDato(self, nombre):
        self.nombre = nombre

    def EliminarDato(self):
        self.nombre = ""


class Coche(object):
    __metaclass__ = ABCMeta
    __marca = ""

    def __init__(self,marca):
        self.__marca = marca

    def getMarca(self):
        return  self.__marca


    @abc.abstractmethod
    def precioMedioCoche(self):
        pass


class Renault(Coche):
    def __init__(self):
        super().__init__('Renualt')

    def precioMedioCoche(self):
        return 18000


class Audi (Coche):
    def __init__(self):
        super().__init__('Audi')

    def precioMedioCoche(self):
        return 25000


class Mercedes(Coche):
    def __init__(self):
        super().__init__('Mercedes')

    def precioMedioCoche(self):
        return 27000

def imprimirCoche(arrayCoches):
    for i in arrayCoches:
        print(str(i.precioMedioCoche())+" "+i.getMarca())

arrayCoches = [ Renault(), Audi(), Mercedes() ]
imprimirCoche(arrayCoches);




