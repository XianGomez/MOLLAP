class Cliente:
    def enviar_peticion(self, usuario):
        raise NotImplementedError("Debes implementar enviar_peticion")

class Mollapp(Cliente):
    def __init__(self):
        self.programador = None

    def set_programador_tareas(self, programador):
        self.programador = programador

    def enviar_peticion(self, usuario):
        if self.programador:
            self.programador.ejecutar_tareas(usuario)
        else:
            print("Error: El cliente no tiene un programador de tareas asignado.")