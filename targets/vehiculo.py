from .target import Target

class Vehiculo(Target):
    def ejecucion(self, usuario):
        print("Puerta abierta", usuario + "!")

