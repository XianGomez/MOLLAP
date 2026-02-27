from administrador.tareas import ProgramadorTareas
from clientes.cliente import Mollapp
from filtros.autenticacion import Autenticacion
from filtros.autorizacion import Autorizacion
from targets.vehiculo import Vehiculo

if __name__ == "__main__":

    coche = Vehiculo()
    programador = ProgramadorTareas(coche)
    
    programador.set_tarea(Autenticacion())
    programador.set_tarea(Autorizacion())
    
    app = Mollapp()
    app.set_programador_tareas(programador)
    
    app.enviar_peticion("ADMIN")