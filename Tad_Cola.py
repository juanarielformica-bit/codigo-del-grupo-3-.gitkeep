def crearCola():
    cola=[]
    return cola
#Crea una cola vacia

def esVacia(cola):
    return len(cola)==0
#Retorna verdadero si la cola no tiene elementos

def encolar(cola,elem):
    cola.append(elem)
#Agrega un elemento al final de cola

def desencolar(cola):
    return cola.pop(0)
#Retorna y elimina el primer elemento de la cola

def tamanio(cola):
    return len(cola)
#Retorna la cantidad de elementos de la cola

def copiarCola(cola1,cola2):
    aux = crearCola()

    while not esVacia(cola2):
        elem=desencolar(cola2)
        encolar(aux,elem)

    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)
        encolar(cola2,elem)
#Copiar los datos de la cola2 a la cola 1
