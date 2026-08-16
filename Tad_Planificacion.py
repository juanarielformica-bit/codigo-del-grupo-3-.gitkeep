from Tad_Orden import*

def crearPlanificacion():
    orden=[]
    return orden
#crea una lista vacia

def agregarDatosTecnicos(orden,s):
    orden.append(s)
#agrega datos tecnicos y de programacion a la planificación

def eliminarDatosTecnicos(orden,s):
    orden.remove(s)
#elimina datos tecnicos y de programacion a la planificación

def recuperar(orden,s):
    return orden[s]
#retorna la orden de la posicion que pasas por parametro

def tamanio(orden):
    return len(orden)
#retorna la cantidad de ordenes

def existesIDM(orden,s):
    return s in orden
#retorna true o false si existe la orden en la planificación
