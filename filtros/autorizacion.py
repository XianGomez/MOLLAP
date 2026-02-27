from .filtro import Filtro

class Autorizacion(Filtro):

    def ejecucion(self, usuario):
        print("Autorizacion OK para", usuario)

