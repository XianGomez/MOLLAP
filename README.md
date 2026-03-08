# MOLLAP

Este proyecto implementa un sistema de control de acceso basado en el patrón de diseño **Intercepting Filter** (Filtro Interceptador). La arquitectura permite procesar peticiones de usuario a través de una cadena de filtros antes de ejecutar una acción final en un objetivo (Target).

## 📊 Arquitectura del Sistema

El proyecto está diseñado siguiendo un diagrama de clases UML que separa las responsabilidades en cuatro módulos principales:

* **Clientes**: El punto de entrada de la petición.
* **Filtros**: Componentes que validan o transforman la petición (Autenticación y Autorización).
* **Administrador**: Coordina la secuencia de filtros y el destino final.
* **Targets**: El recurso final al que se desea acceder (Vehículo).



---

## 📂 Estructura de Directorios

```text
.
├── administrador/
│   └── tareas.py        # Clases Tareas y ProgramadorTareas
├── clientes/
│   └── cliente.py       # Clase Mollapp (Cliente)
├── filtros/
│   ├── filtro.py        # Clase base Filtro
│   ├── autenticacion.py  # Lógica de Autenticación
│   └── autorizacion.py   # Lógica de Autorización
├── targets/
│   ├── target.py        # Clase base Target
│   └── vehiculo.py      # Clase Vehiculo (Objetivo final)
└── main.py              # Script de ejecución y prueba
```
🚀 Instalación y Ejecución
Clonar el repositorio:

Bash
git clone https://github.com/XianGomez/Mollap.git
Entrar al directorio:

Bash
cd MOLLAP
Ejecutar la aplicación:

Bash
python main.py
🛠️ Detalle de Implementación
El flujo de información se gestiona mediante el paso de un parámetro usuario. El proceso sigue este orden exacto:

El cliente Mollapp envía el usuario "ADMIN".

El ProgramadorTareas recibe la petición y dispara la lista de tareas.

Se ejecuta el filtro de Autenticación.

Se ejecuta el filtro de Autorización.

Si la cadena se completa, el Vehiculo ejecuta la acción de abrir la puerta.

Ejemplo de Salida en Consola:
Plaintext
Autenticación OK para ADMIN
Autorización OK para ADMIN
Puerta abierta ADMIN!
