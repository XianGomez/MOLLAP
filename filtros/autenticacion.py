from .filtro import Filtro

class Autenticacion(Filtro):

    def ejecucion(self, usuario):
        print("Autenticacion OK para", usuario)
