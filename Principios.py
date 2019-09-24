class Coche():
    __marca = ""

    def __init__(self,marca):
        self.__marca = marca

    def getMarca(self):
        return  self.__marca





class CocheBD():
    nombre = ""
    def GuardarDato(self, nombre):
        self.nombre = nombre



    def EliminarDato(self):
        self.nombre = ""

