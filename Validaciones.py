from Tad_Orden import*
from datetime import datetime, date
import unicodedata

def validarTexto(orde):             
    texto=orde.strip()                                          #Borra los espcaios libres que hayan quedado al principio o al final
    if any(c.isalpha() for c in texto):                         #1er filtro. Si existe almenos una letra
        if all(c.isalpha() or c.isspace() for c in texto):      #2do filtro. Si en texto solo hay letras o espacios intermedios (debido al strip previo)
               return True                                      #Caso Correcto
        else:
            print("Error: La Orden debe ser con Caracteres.")
            return False
    else:
        print("Error: La Orden debe contener Caracteres.")
#esta validacion, solo acepta caracteres y espacios
    
def validarNumerico(idm):
    try:                                                                          #Intenta transformar el String a un número entero
        valor = int(idm)
        if valor>0:                                                               #Si el valor es positivo...
            return True                                                           #Caso Correcto
        else:
            print("Error: El ID debe ser un valor Númerico entero positivo.")
            return False                                                          #Si el int() falló porque el usuario metió datos no validos, cae acá
    except ValueError:
        print("Error: No Ingresó Números válido para el ID de la Máquina.")
        return False
#Esta validacion funciona, descarta todo aquello que no sea, un numero entero positivo
    

def validarFecha(fecha_Ingresada, fecha_Hoy):
    # Recibe fecha_texto: como un string.
    # Recibe fecha_actual_objeto: como objeto de tipo date
    try:                                
        fecha = datetime.strptime(fecha_Ingresada, "%d/%m/%Y").date()               #Conversión de la fecha ingresada (string) a objeto y lo guarda en variable fecha(para comparar)

        if fecha >= fecha_Hoy:                                                      #Compara matemáticamente la fecha ingresada(fecha) y fecha de hoy, ambos de tipo objeto date
            return True                                                             #La fecha es hoy o a futuro
        
        else:                                                                       #Si la fecha ingresada resulta ser menor(antes) que la de hoy...
            print("Error: la fecha no puede ser anterior a hoy.")
            return False
    except ValueError:                  
        print("Error: formato inválido. Ejemplo correcto: 09/12/2018.")
        return False
#Esta Validacion recibe como parametros la fecha ingresada (como string)y la fecha de hoy
#transforma en objeto la fecha ingresada para poder compararla con la actual y verificar que la fecha a programar sea posterior al dia de hoy


def validarHora(hora_Ingresada, hora_Actual):
    try:
        hora= datetime.strptime(hora_Ingresada, "%H:%M").time()         #Transforma hora ingresado (primer parametro tipo string) a objeto time

        if hora >= hora_Actual:                                         #Si la hoa ingresada (ahora objeto) es posterior a la actual
            return True
        else:
            print("Error: la Hora no puede ser anterior a la actual.")
            return False
    except ValueError:
        print("Error: formato inválido. Ejemplo correcto: 10:25.")
        return False

#Esta Validacion recibe como parametros la hora ingresada y la hora actual
#transforma la hora actual en un objeto, para poder compararla con la actual

def validar_Nueva_Fecha(fecha_Ingresada, fecha_Hoy, fecha_Anterior):
    try:                                                                #Intenta parsear la cadena ingresada al formato DD/MM/AAAA y extrae solo la fecha (objeto date)
        fecha = datetime.strptime(fecha_Ingresada, "%d/%m/%Y").date()

        if fecha == fecha_Anterior:                                     #Valida que la fecha propuesta no sea idéntica a la que ya tiene asignada la orden
            print("Error: la fecha no puede ser igual a la anterior.")
            
            return False                                                #Rechaza la modificación por redundancia de datos
        elif fecha < fecha_Hoy:                                         #Valida que la fecha elegida no sea cronológicamente anterior al día de hoy
            
            print("Error: la fecha no puede ser anterior a hoy.")
            return False                                                #Rechaza la modificación para evitar registros en el pasado

        else:
            return True                                                 #La fecha cumple con todos los filtros lógicos de la planificación

    except ValueError:                                                  #Captura errores si el string ingresado no coincide con la máscara de formato o es una fecha inexistente (ej: 31/02)
        print("Error: formato inválido. Ejemplo correcto: 12/07/2026.")
        return False                                                    #Retorna Falso para mitigar un posible colapso del programa ante entradas inválidas
#version modificada de la anterior fecha, esta no permite que se pueda volver
#a modificar la fecha en la que ya estaba


def validar_Nueva_Hora(hora_Ingresada, hora_Actual, hora_Anterior):
    try:                                                                #Intenta transformar la cadena ingresada en un objeto de tiempo abstracto (objeto time: HH:MM:SS)
        hora= datetime.strptime(hora_Ingresada, "%H:%M").time()

        if hora == hora_Anterior:                                       #Evita que el usuario cargue exactamente la misma hora que la orden ya tenía asignada
            print ("Error: la Hora no puede ser igual a la anterior. ")

            return False                                                #Cancela la operación por redundancia en la modificación

        elif hora< hora_Actual:                                         #Controla que el nuevo horario de mantenimiento no pertenezca al pasado en el día de hoy
            print ("Error: la Hora no puede iniciar en un horario anterior al actual")
            return False                                                #Deniega el cambio porque la hora del sistema ya avanzó más allá de ese límite

        else:
            return True                                                 #La hora pasó los filtros de consistencia cronológica del sistema

    except ValueError:                                                  #Atrapa errores de sintaxis en el string o números fuera de rango (ej: "25:70" o letras)
        print("Error: formato inválido. Ejemplo correcto: 10:25.")
        return False                                                    #Retorna Falso para mitigar una interrupción abrupta (crash) del programa

#version modificada de la anterior hora, esta no permite que se vuelva a poner
#la hora que ya estaba


def validarHorario(hora_Ingresada):
    try:                                                                #Si la cadena no respeta el formato HH:MM o tiene números inválidos (ej: "26:00"), lanza un ValueError
        datetime.strptime(hora_Ingresada, "%H:%M")
        return True                                                     #La estructura sintáctica del string es correcta y representa un horario válido
        
    except ValueError:                                                  #Filtra errores léxicos o de tipeo por teclado (letras, símbolos o formatos incorrectos)
        print("Error: formato inválido. Ejemplo correcto: 10:25.")
        return False                                                    #Evita el colapso (crash) del sistema retornando un estado lógico de rechazo

def validar_Nuevo_Horario(hora_Ingresada, hora_Anterior):
    try:                                                                #Intenta convertir el string ingresado en un objeto de tiempo abstracto (objeto time: HH:MM:SS)
        hora = datetime.strptime(hora_Ingresada, "%H:%M").time()
        if hora == hora_Anterior:                                       #Controla que la nueva hora propuesta sea diferente a la hora histórica del registro
            print("Error: la Hora no puede ser igual a la anterior. ")
            return False                                                #Rechaza la modificación por redundancia de datos
        else:
            return True                                                 #El horario es sintácticamente correcto y cambia el estado anterior del cronograma

    except ValueError:                                                  #Atrapa cualquier anomalía de formato en el texto ingresado
        print("Error: formato inválido. Ejemplo correcto: 10:25.")
        return False

def normalizar_mayus(a):
    a=a.upper()                                                     #Convierte toda la cadena de texto a letras mayusculas
    a=unicodedata.normalize("NFD", a)                               #Separa las letras con acento en dos partes: la letra base y el acento flotante
    a="".join(c for c in a if unicodedata.category(c) != "Mn")      #recorre la cadena carácter por carácter y deja pasar solo a los que NO sean ecpacios ni acentos, y luego no reconstruye. => (Mark, Nonspacing)
    return a                                                        #Retorna Falso para mitigar interrupciones en el flujo principal
