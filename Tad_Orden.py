
def crearOrdenTrabajo():
    orden =[" ",0," "," "," ",0,0]
    return orden
    #crear y retorna un sector de trabajo sin datos



def registrarOrdenTrabajo(orden,o,idm,nomequipo,sectorp,tecniasi,fechap, horaini):
    orden[0]=o
    orden[1]=idm
    orden[2]=nomequipo
    orden[3]=sectorp
    orden[4]=tecniasi
    orden[5]=fechap
    orden[6]=horaini
    #carga los datos de orden de trabajo

def verOrden(orden):
    return orden[0]
#retorna la orden 

def verIDM(orden):
    return orden[1]
#retorna el id de la maquina 

def verNomEquipo(orden):
    return orden[2]
#retorna el nombre del equipo

def verSectorP(orden):
    return orden[3]
#retorna el sector de la planta

def verTecniAsi(orden):
    return orden[4]
#retorna el tecnico asignado

def verFechaP(orden):
    return orden[5]
#retorna la fecha programada

def verHoraIni(orden):
    return orden[6]
#retorna la hora de inicio

def modificarOrden(orden,otros):
    orden[0]=otros
#modifica la orden 

def modificaIDM(orden,otros):
    orden[1]=otros
#modifica el id de una maquina

def modificaNomEquipo(orden,otros):
    orden[2]=otros
#modifica el nombre del equipo

def modificaSectorP(orden,otros):
    orden[3]=otros
#modifica el sector de la planta

def modificaTecniAsi(orden,otros):
    orden[4]=otros
#modifica al tecnico asignado

def modificaFecha(orden,otros):
    orden[5]= otros
#modifica la fecha programada

def modificaHoraIni(orden,otros):
    orden[6]= otros
#modifica la hora de inicio
    
