class Tareas():

    def __init__(self):
        self.filtros = []
        self.target = None
    
    def añadir_tarea(self, filtro):
        self.filtros.append(filtro)

    def set_target(self, target):
        self.target = target

    def ejecucion(self, usuario):
        for filtro in self.filtros:
            filtro.ejecucion(usuario)

        if self.target:
            self.target.ejecucion(usuario)

class ProgramadorTareas:
    def __init__(self, target):
        self.tareas = Tareas()
        self.tareas.set_target(target)

    def get_tareas(self):
        return self.tareas

    def set_tarea(self, filtro):
        self.tareas.añadir_tarea(filtro)

    def ejecutar_tareas(self, usuario):
        self.tareas.ejecucion(usuario)