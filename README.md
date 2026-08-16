# Sistema de Gestión de Órdenes de Mantenimiento

**Desarrollado para:** UTN – Sintaxis de Lenguajes  
**Grupo:** 3  
**Autor:** juan formica


---

##  Descripción general

Sistema de planificación y gestión de órdenes de trabajo para mantenimiento industrial.  
Permite registrar, modificar, cancelar y reprogramar tareas de mantenimiento en una planta, administrando técnicos, máquinas, sectores y cronogramas.

Fue desarrollado en Python, aplicando **Tipos Abstractos de Datos (TAD)** y una arquitectura modular.

---

##  Características

- **Alta de órdenes de trabajo:** Registra nuevas tareas con validación de datos y control de solapamiento de horarios.
- **Modificación de cronograma:** Cambia fecha y/o hora de una orden existente.
- **Cancelación de tareas:** Elimina órdenes por ID de máquina, fecha/hora, o técnico asignado (con justificación).
- **Reporte general:** Muestra todas las órdenes almacenadas de forma ordenada.
- **Reprogramación por parada de planta:** Mueve todas las órdenes de una fecha a otra nueva, de forma masiva.
- **Depuración y lista de prioridad:** 
  - Baja por sector (elimina todas las órdenes de un sector).
  - Generación de cola de intervención (muestra el orden de salida de técnicos para un día específico).
- **Validaciones robustas:** Control de fechas, horarios, solapamiento de equipos, y técnicos.

---

## Tecnologías utilizadas

- Python 3
- Módulos: `datetime`, `unicodedata`
- Estructuras de datos: listas (TADs), colas

---

##  Estructura del código

codigo_del_grupo_3/


├── Sistema de Gestión de Órdenes de Mantenimiento.py # Programa principal (menú y lógica)

├── Tad_Cola.py # TAD de cola

├── Tad_Orden.py # TAD de orden de trabajo

├── Tad_Planificacion.py # TAD de planificación (lista de órdenes)

└── Validaciones.py # Funciones de validación de datos



---

##  Cómo ejecutarlo

1. Cloná este repositorio o descargá los archivos.
2. Asegurate de tener **Python 3** instalado.
3. Abrí una terminal en la carpeta donde descargaste el proyecto.
4. Ejecutá el archivo principal con el siguiente comando:

 ```bash
   python "codigo_del_grupo_3/Sistema de Gestión de Órdenes de Mantenimiento.py"

## Prácticas en C

Además del proyecto principal, también subo algunos de mis primeros programas en C,
como este simulador de torre de control, que fue mi primer acercamiento a un sistema en tiempo real.

**Nota:** No es funcional al 100%, pero es el testimonio de mi evolución.  
**Materia :** Algoritmos y Estructuras de Datos.
