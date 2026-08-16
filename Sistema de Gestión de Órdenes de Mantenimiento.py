""" Cada orden de trabajo deberá contener la siguiente información:
ID de Máquina, Nombre del Equipo, Sector de la Planta, Técnico Asignado,
Fecha Programada y Hora de Inicio.

El sistema deberá brindar un menú de opciones

1_ alta de ordenes de trabajo : Registra nuevas ordenes de trabajo de mantenimiento, ingresando todos los datos tecnicos y de programacion correspondientes

2_ modificación de cronograma: modifica la fecha y/o hora de un trabajo ya existente, identificando la misma mediante id de la maquina

3_ canceacion de tareas: elimina una orden de trabajo especifica de la planificacion, ya sea por falta de respuesta o por cambio en la prioridad de la planta

4_ reporte general de mantenimiento: muestra todas las ordenes de trabajo almacenadas, desplegando ordenamente todos los datos de cada invencion programada

5_ reprogramacion por parada de planta(translado masivo) : permite mover, todas las ordenes de trabajo de una fecha determinada a una nueva fecha, facilitando la
reorganizacion del equipo tecnico ante contigencias o paradas de planta no programada

6_ depuracion y generacion de lista de prioridad:

* baja por sector : elimina todas las ordenes de trabajo asociadas a un sector de planta ingresado por el usuario

* generacion de cola de intervención: genera una nueva cola que contenga unicamente el nombre del equipo y el tecnico asignado de todos para un dia especifico
esta cola representa el orden de salida de los tecnicos del talle y debe imprimirse por pantalla
"""
#Tad y Funciones auxiliares
from Tad_Planificacion import*
from datetime import datetime, date
from datetime import datetime, timedelta
from Tad_Cola import*
from Validaciones import*

#Inicio del Programa
print("///////////////////////////////////////////////////////////////\n\n")
print ("Bienvenido al Sistema de Gestión de Órdenes de Mantenimiento \n")
print("///////////////////////////////////////////////////////////////\n\n")

#Se crea una Planificación con el Tad Compuesto
o=crearPlanificacion()

orden0= crearOrdenTrabajo()
registrarOrdenTrabajo(orden0,"REPARAR SOPLADORA", "00001","EQUIPO 0","Fundición","CARLOS MENDOZA","17/08/2026","05:00")

orden1= crearOrdenTrabajo()
registrarOrdenTrabajo(orden1,"RERARAR FUNDIDORA", "00001","EQUIPO 0","Fundición", "CARLOS MENDOZA","17/06/2026", "06:00")

orden2= crearOrdenTrabajo()
registrarOrdenTrabajo(orden2,"REPARAR HORNO","00002","EQUIPO 1","Embalaje", "MARCOS L","18/06/2026","07:00")

orden3= crearOrdenTrabajo()
registrarOrdenTrabajo(orden3,"REPARAR CLARK","00003","EQUIPO 2","Deposito","SANTIAGO A","17/06/2026","09:15")

orden4= crearOrdenTrabajo()
registrarOrdenTrabajo(orden4,"REVISION DE RUTINA","00004","EQUIPO 3","Producción","TOMAS L","17/06/2026","08:00")

orden5= crearOrdenTrabajo()
registrarOrdenTrabajo(orden5,"REVISAR VALVULA DOS","00005","EQUIPO 4","Producción","ALBERTO P","18/06/2026","14:00")

orden6= crearOrdenTrabajo()
registrarOrdenTrabajo(orden6,"REVISAR TOLVA","00006","EQUIPO 5","Producción","ALEXANDER C","12/12/2026","05:00")

orden7= crearOrdenTrabajo()
registrarOrdenTrabajo(orden7,"REVISAR CALDERA","00007","EQUIPO 6","Fundición","GIAN L","18/08/2026","07:00")

orden8= crearOrdenTrabajo()
registrarOrdenTrabajo(orden8,"REVISAR PRESION","00008","EQUIPO 7","Fundición","FRANCESCO V","20/08/2026","06:00")

orden9= crearOrdenTrabajo()
registrarOrdenTrabajo(orden9,"REPARAR GILLOTINA","00009","EQUIPO 8","Embalaje","JUAN C","17/06/2026","09:30")

orden10= crearOrdenTrabajo()
registrarOrdenTrabajo(orden10,"REPARAR ETIQUETADORA","00010","EQUIPO 9","Producción","PEDRO L","19/06/2026","08:00")

orden11= crearOrdenTrabajo()
registrarOrdenTrabajo(orden11,"REVISAR LOTEADORA","00011","EQUIPO 10","Producción","IGNACIO E","20/12/2026","20:00")

orden12= crearOrdenTrabajo()
registrarOrdenTrabajo(orden12,"REPARAR ETIQUETADORA","00012","EQUIPO 11","Producción","PEDRO L","29/06/2026","07:00")

orden13= crearOrdenTrabajo()
registrarOrdenTrabajo(orden13,"REVISAR LOTEADORA","00013","EQUIPO 12","Producción","IGNACIO E","29/12/2026","06:00")

orden14= crearOrdenTrabajo()
registrarOrdenTrabajo(orden14,"REVISAR TOLVA","00014","EQUIPO 13","Producción","ALEXANDER C","29/12/2026","05:00")

agregarDatosTecnicos(o, orden0)
agregarDatosTecnicos(o, orden1)
agregarDatosTecnicos(o, orden2)
agregarDatosTecnicos(o, orden3)
agregarDatosTecnicos(o, orden4)
agregarDatosTecnicos(o, orden5)
agregarDatosTecnicos(o, orden6)
agregarDatosTecnicos(o, orden7)
agregarDatosTecnicos(o, orden8)
agregarDatosTecnicos(o, orden9)
agregarDatosTecnicos(o, orden10)
agregarDatosTecnicos(o, orden11)
agregarDatosTecnicos(o, orden12)
agregarDatosTecnicos(o, orden13)
agregarDatosTecnicos(o, orden14)
    
opcion="1"
while(opcion!="8"):
    print("///////////////////////////////////////////////////////////////\n\n")
    print("Sistema de menú de opciones: \n")
    print("///////////////////////////////////////////////////////////////\n\n")
    print("Elija el proceso que desee llevar a cabo\n")
    print("1_  Alta de Órdenes de Trabajo.\n")
    print("2_  Modificación de Cronograma.\n")
    print("3_  Cancelación de Tareas.\n")
    print("4_  Reporte General de Mantenimiento.\n")
    print("5_  Reprogramación por Parada de Planta.\n")
    print("6_  Depuración y Generación de Lista de Prioridad.\n")
    print("7_  Mostrar todas las órdenes vigentes.\n")
    print("8_  Finalizar Programa.\n")
    opcion=input("Elige una opción: ")
    valido = False

    #primera opción del menú
    if(opcion=="1"):

        s=crearOrdenTrabajo()
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Alta de órdenes de Trabajo.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")
        #pide ingresar la orden,y valida texto para que solo se pueda escribir con caracteres
        while not valido:
            orde=normalizar_mayus(input("\nIngrese la Orden que desee ejecutar:"))
                             
            if(validarTexto(orde) ):
               print("[Ingreso Correcto de la Orden.]\n")
               print("\nLa Orden cargada es : ",orde)
               valido = True

            else:
                
                print("\n\n-------Vuelva a intentarlo.---------")

        #pide ingresar el id de maquina y valida para que solo se puedan colocar numeros enteros positivos en él
        print("\n---------------------------------------------------------------------------\n")
        valido = False
        while not valido:
            i=input("\nIngrese el Número ID de la Máquina:")

            
        
            if (validarNumerico(i)):
                
                    print("\n[Ingreso Correcto del Número ID de la Máquina].\n")
                    print("\nEl Número ID de la Máquina es :",i)
                    valido = True
            else:
                print("\n\n-------Vuelva a intentarlo.---------")
                
        #pide ingresar el nombre del equipo y valida que solo sea utilizado caracteres y espacios
        print("-----------------------------------------------------------------------------\n")
        valido = False 
        while not valido:
            n=normalizar_mayus(input("\nIngrese el Nombre del Equipo:"))

        
            if(validarTexto(n)):
                
                    print("\n[Ingreso Correcto del Nombre del Equipo.]\n")
                    print("\nEl Nombre del Grupo es : ",n)
                    valido = True
            else:
                print("\n\n-------Vuelva a intentarlo.---------")


        #submenu con varias opciones para elegir como sector
        print("-----------------------------------------------------------------------------\n")
        valido=False
        while not valido:
            print("\n Elija el Sector de la Planta: \n")
            print("1_  Producción.\n")
            print("2_  Embalaje.\n")
            print("3_  Fundición.\n")
            print("4_  Deposito.\n")

            
            se=input("\nIngrese el Sector de la Planta:")

            if(se == "1"):
                print("\n\n[Ingreso Correcto del Sector de la Planta: Producción.]\n")
                se = "Producción"
                valido = True

            elif(se == "2"):
                print("\n\n[Ingreso Correcto del Sector de la Planta: Embalaje.]\n")
                se= "Embalaje"
                valido = True
                

            elif(se == "3"):
                print("\n\n[Ingreso Correcto del Sector de la Planta: Fundición.]\n")
                se= "Fundición"
                valido = True

            elif(se == "4"):
                print("\n\n[Ingreso Correcto del Sector de la Planta: Deposito.]\n")
                se = "Deposito"
                valido = True
                
            else:
                print("\n\n-------Vuelva a intentarlo.---------")
        
        #pide ingresar un tecnico y valida que solo sea texto con espacios lo que se haya puesto
        print("-----------------------------------------------------------------------------\n")
        valido = False 
        while not valido:
            t=normalizar_mayus(input("\nIngrese el Técnico Asignado:"))


            if(validarTexto(t)):
                
                    print("\n[Ingreso Correcto del Técnico Asignado.]\n")
                    print("\nEl Tecnico Asignado es : ",t)
                    valido = True
            else:
                print("\n\n-------Vuelva a intentarlo.---------")
        
        

        #pide la fecha y tiene que ser si o si mayor o igual a la actual, si detecta que hay algunas coincidencias entonces te pide ingresar otra fecha distinta
        print("-----------------------------------------------------------------------------\n")
        valido = False 
        while not valido:
            
            fecha_Hoy = date.today()
                     

            entradaF= input(f"\nIngrese la Fecha Programada (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")

            buscado=(n)
            encontrado = None

            pos = 0
            
            while pos< tamanio(o) and encontrado is None:
                b= recuperar(o,pos)

                if verNomEquipo(b)== buscado:
                             encontrado =b
                pos +=1

            
            
            if(validarFecha(entradaF, fecha_Hoy)):
                if (encontrado is not None and verNomEquipo(encontrado) == n and verTecniAsi(encontrado) == t and verFechaP(encontrado)== entradaF ):
                    print("\n El Nombre del grupo ingresado no no puede ser igual al de otro equipo cargado con anterioridad.\n Tampoco se puede asignar el mismo tecnico a otra tarea diferente, en el mismo dia. \n")
                elif(encontrado is not None and verNomEquipo(encontrado) == n and verFechaP(encontrado) == entradaF):
                    print("\n El Nombre del grupo ingresado no puede ser igual al de otro cargado con anterioridad en el mismo dia.\n")
                elif(encontrado is not None and verTecniAsi(encontrado)== t and verFechaP(encontrado)== entradaF):
                    print("\n No puede volver a asignar el mismo Tecnico, a otra tarea diferente el mismo dia.\n")
                else:
                    print("\n[Ingreso Correcto de La Fecha Programada.]\n")
                    print("\nLa Fecha programada es : ",entradaF)
                    fecha_Anterior_Str= entradaF
                    fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()
                    valido = True
            else:
                print("\n\n-------Vuelva a intentarlo.---------")

        #pide ingresar la hora, si hay otra hora ocupando ese lugar en el mismo sector tira una alerta diciendo que el sector y la maquina estan ocupada por al menos 1 hora
        #como la hora es dependiente de la fecha, si sobrepasa las 23 horas entonces te deja modificarla, si elegis que no, te tira y hace que cargues todos los datos devuelta

        print("-----------------------------------------------------------------------------\n")
        valido = False 
        while not valido:
            
            hora_Actual = datetime.now().time()
            sigue_Dia=0

            entradaH= input(f"\nIngrese la Hora de Inicio (HH:MM). Hora Actual es [{hora_Actual.strftime('%H:%M')}]: ")
            
            if (fecha_Anterior == fecha_Hoy):
                if(validarHora(entradaH, hora_Actual)):
                    #la idea de esto es restringir el horario por un intervalo de tiempo, sumarle por ejemplo 3 horas restrintiva que es cuando se usa la maquina
                    #el sector y el horario que coincide, entonces con eso evitaria el solapamiento 
                    nuevaHora= datetime.strptime(entradaH, "%H:%M").time()
                    inicioNuevo=datetime.combine(datetime.today(),nuevaHora)
                    finNuevo=inicioNuevo+timedelta(hours=1)
                    pos=0
                    horario=False
                    
                    while pos <tamanio(o):
                        b= recuperar(o,pos)
                        
                        
                        if(verSectorP(b) == se and verFechaP(b) == entradaF):##########################
                            horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                            inicioExistente = datetime.combine(datetime.today(), horaExistente)
                            finExistente= inicioExistente + timedelta(hours=1)

                            if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                print("\nLa Máquina de este sector ya ha sido Asignados para este horario.\n Cargue un Horario diferente.\n")
                                print("\nSe Especula que la Máquina tardara en desocuparse en aproximadamente 1 Hora.")
                                if (hora_Actual >= datetime.strptime("23:00", "%H:%M").time()):
                                    print("\n\nQuiere pasar la fecha para el dia siguiente?")
                                    print("\n1_ Si.\n")
                                    print("\n2_ No. \n")
                                    sigue_Dia=(input("\nIngrese la opción:"))

                                    if(sigue_Dia == "1"):
                                                              print("Modifica Fecha")
                                                              print("\n---------------------------------------------------------------------------\n")
                                                              modificado = False 
                                                              while not modificado:
                                                                  fecha_Hoy = date.today()
                                                                  entradaF= input(f"\nIngrese la Fecha Programada (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")
                                                                  buscado=(n)
                                                                  encontrado = None
                                                                  pos = 0
            
                                                                  while pos< tamanio(o) and encontrado is None:
                                                                      b= recuperar(o,pos)

                                                                      if verNomEquipo(b)== buscado:
                                                                          encontrado =b
                                                                      pos +=1

            
            
                                                                  if(validarFecha(entradaF, fecha_Hoy)):
                                                                      
                                                                      if (encontrado is not None and verNomEquipo(encontrado) == n and verTecniAsi(encontrado) == t and verFechaP(encontrado)== entradaF ):
                                                                          print("\n El Nombre del grupo ingresado no no puede ser igual al de otro equipo cargado con anterioridad.\n Tampoco se puede asignar el mismo tecnico a otra tarea diferente, en el mismo dia. \n")
                                                                      elif(encontrado is not None and verNomEquipo(encontrado) == n and verFechaP(encontrado) == entradaF):
                                                                          print("\n El Nombre del grupo ingresado no puede ser igual al de otro cargado con anterioridad en el mismo dia.\n")
                                                                      elif(encontrado is not None and verTecniAsi(encontrado)== t and verFechaP(encontrado)== entradaF):
                                                                          print("\n No puede volver a asignar el mismo Tecnico, a otra tarea diferente el mismo dia.\n")
                                                                      elif(entradaF == fecha_Hoy):
                                                                          print("\n\nNo se puede volver a utilizar la fecha de hoy.\n") 
                                                                      else:
                                                                           print("\n[Ingreso Correcto de La Fecha Programada.]\n")
                                                                           print("\nLa Fecha programada es : ",entradaF)
                                                                           fecha_Anterior_Str= entradaF
                                                                           fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()
                                                                           modificado = True
                                                                  else:
                                                                           print("\n\n-------Vuelva a intentarlo.---------")
                    
                                    elif(sigue_Dia == "2"):
                                        print("\n\nError, vuelva a cargar todos los datos.\n")
                                        print("\n\n-----Volve a ingresar todos los datos desde el inicio.----------\n")
                                        valido=True
                                    else:
                                        print("\n\nError, vuelva a cargar todos los datos. \n")
                                        print("\n\n-----Volve a ingresar todos los datos desde el inicio.----------\n")
                                        valido=True
                                        sigue_Dia =="2"
                                horario= True
                        pos+=1
                

                    if not horario:
                        print("[Ingreso Correcto de la Hora de Inicio.]\n")
                        print("\nHora de Inicio asignada: ", entradaH)
                        valido = True
                    
                else:
                    print("-------Vuelva a intentarlo.---------")

            else:
                if(validarHorario(entradaH)):
                    nuevaHora= datetime.strptime(entradaH, "%H:%M").time()
                    inicioNuevo=datetime.combine(datetime.today(),nuevaHora)
                    finNuevo=inicioNuevo+timedelta(hours=1)
                    pos=0
                    horario=False
                    
                    while pos <tamanio(o):
                        b= recuperar(o,pos)
                        
                        
                        if(verSectorP(b) == se and verFechaP(b) == entradaF):
                            horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                            inicioExistente = datetime.combine(datetime.today(), horaExistente)
                            finExistente= inicioExistente + timedelta(hours=1)

                            if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                print("\nLa Máquina de este sector ya ha sido Asignados para este horario.\n Cargue un Horario diferente.\n")
                                print("\nSe Especula que la Máquina tardara en desocuparse en aproximadamente 1 Hora.")
                                horario= True
                        pos+=1
                

                    if not horario:
                        print("[Ingreso Correcto de la Hora de Inicio.]\n")
                        print("\nHora de Inicio asignada: ", entradaH)
                        valido = True
                    
                    
                else:
                    print("\n\n-------Vuelva a intentarlo.---------")
        
        #guarda los datos en el tad simple
        if(sigue_Dia == "2"):
            print("Vuelva a intentarlo.\n")
        else:
            registrarOrdenTrabajo(s,orde,i,n,se,t,entradaF,entradaH)
        #agrega datos al tad compuesto
            agregarDatosTecnicos(o,s)
        
    #segunda opción del menú
    elif(opcion=="2"):

        #segundo submenú
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Modificación de Cronograma.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")

        print("-----Elija la opción que desea modificar----\n")

        print("1_  Fecha.\n")
        print("2_  Hora.\n")
        print("3_  Fecha y Hora.\n")
        print("4_  Regresar al menú principal. \n")
        opci=input("Elige una opción: ")

        if(opci == "1"):
            print("Modifica Fecha")
            print("\n---------------------------------------------------------------------------\n")
            valido = False
            if(tamanio(o)==0):
                print("\n\nNo se puede modificar la fecha, si no hay Ordenes programadas.\n")
                valido=True
            while not valido:
                
                i=input("\nIngrese el Número ID de la Máquina que quiera identificar :")
                #modifca la fecha a través del id de la maquina, si existe, entonces te deja elegir otra fecha y pregunta confirmacion, por si o por no
                #no deja que se sobrepongan ordenes, si es en el mismo sector, si hay más fechas programadas con esa id de la maquina, te pide que utilices la opcion más especifica
                if (validarNumerico(i)):
                         
                    buscado=(i)
                    encontrado = None
                    pos = 0
                    mismamaq=0

                    while pos < tamanio(o) :      
                        b = recuperar(o,pos)
                
                        if verIDM(b) == buscado:
                            
                            encontrado= b
                            mismamaq+=1

                        pos += 1
                
                    if encontrado and mismamaq == 1:
                        
                        
                        print("\n\nExiste el Número ID de la Máquina. ")

                        print("-----------------------------------------------------------------------------\n")
                        valido = False 
                        while not valido:
                            fecha_Hoy = date.today()
                            fecha_Anterior_Str= verFechaP(encontrado)
                            fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()
                            
                            print("\nLa fecha programada anteriormente es : ",verFechaP(encontrado))
                            nueva_EntradaF= input(f"\n\nIngrese la Nueva Fecha Programada (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")


                            
                            if(validar_Nueva_Fecha(nueva_EntradaF, fecha_Hoy,fecha_Anterior)):
                                inicioNuevo=datetime.combine(datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(),datetime.strptime(verHoraIni(encontrado), "%H:%M").time())
                                finNuevo=inicioNuevo+timedelta(hours=1)
                                pos=0
                                horario=False
                    
                                while pos <tamanio(o):
                                    b= recuperar(o,pos)
                        
                                    if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == nueva_EntradaF):
                                        horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                        inicioExistente = datetime.combine (datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(), horaExistente)
                                        finExistente= inicioExistente + timedelta(hours=1)

                                        if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                            print("\nHay otra Máquina que ya tiene el horario asignado en esa Fecha.\n Cargue un Horario diferente.\n")
                                            horario= True
                                    pos+=1
                

                                if not horario:
                                    print ("\nSeguro qué quiere modificar la Fecha?")
                                    print ("\n1_ Si")
                                    print("\n2_ No\n\n")
                                    a = input("Elija  una opción: ")
                
                                    if (a == "1"):
                                        print("\n[Ingreso Correcto de La Nueva Fecha Programada.]")
                                        print("\nLa Nueva Fecha Programada es : ",nueva_EntradaF)
                                        modificaFecha(encontrado,nueva_EntradaF)
                                        valido = True

                                    elif(a =="2"):
                                        print("\n\nRegresando al menú principal. \n")
                                        valido=True

                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")
                          


                            else:
                                print("\n\n-------Vuelva a intentarlo.---------")
        
                    elif(mismamaq >1):
                        print("\n\nLa Máquina buscada contiene varias Fechas asignadas.\nElija la opción de Modificación por fecha y hora.\n")
                        valido = True

                    else:
                            
                        print ("\nNo se encontró ninguna orden identificada con ese ID de Máquina.\n")
                            
                        valido = True
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\n-------Regresando al Menu Principal.---------")
                    valido = True

                

            
          #modificar hora, pregunta por el id de la maquina, si existe te deja poner un horario y pide confirmacion, por si o por no
          #tiene validaciones para evitar que se pisen los horarios en los mismos sectores

        elif(opci=="2"):
             print("Modifica Hora.")
             print("\n---------------------------------------------------------------------------\n")
             valido = False
             if(tamanio(o)==0):
                print("\n\nNo se puede modificar la hora, si no hay Ordenes programadas.\n")
                valido=True
             while not valido:
                i=input("\nIngrese el Número ID de la Máquina que quiera identificar :")


                if (validarNumerico(i)):
                    buscado=(i)
                    encontrado = None

                    pos = 0
                    mismamaq=0
                    while pos < tamanio(o):
                        
                            
                        b = recuperar(o,pos)
                
                        if verIDM(b) == buscado:
                            
                            encontrado= b
                            mismamaq+= 1
                        pos += 1
                
                    if encontrado and mismamaq == 1 :
                        
                        print("Existe el Número ID de la Máquina. ")

                        print("-----------------------------------------------------------------------------\n")
                        valido = False 
                        while not valido:
                                
#########  
                            hora_Actual = datetime.now().time()
                     
                            hora_Anterior_Str= verHoraIni(encontrado)
                            hora_Anterior=datetime.strptime(hora_Anterior_Str, "%H:%M").time()

                            print("\nLa Hora de inicio programada anteriormente es : ",verHoraIni(encontrado))
                     
                            nueva_EntradaH= input(f"\nIngrese la Nueva Hora de Inicio (HH:MM). Hora Actual es [{hora_Actual.strftime( '%H:%M')}]: ")

                            fecha_Hoy = date.today()
                            fecha_Anterior_Str= verFechaP(encontrado)
                            fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                            if (fecha_Anterior == fecha_Hoy):
                                
                                if(validar_Nueva_Hora(nueva_EntradaH, hora_Actual,hora_Anterior)):
                                    fechaNueva=datetime.strptime(verFechaP(encontrado), "%d/%m/%Y").date()
                                    nuevaHora= datetime.strptime(nueva_EntradaH, "%H:%M").time()
                                    inicioNuevo=datetime.combine(fechaNueva, nuevaHora)
                                    finNuevo=inicioNuevo+timedelta(hours=1)
                                    pos=0
                                    horario=False
                    
                                    while pos <tamanio(o):
                                        b= recuperar(o,pos)
                                        if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == verFechaP(encontrado )):
                                           horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                           inicioExistente = datetime.combine(fechaNueva, horaExistente)
                                           finExistente= inicioExistente + timedelta(hours=1)

                                           if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                               print("\nHay una Máquina de este sector ya ha sido Asignados para este horario.\n\nCargue un Horario diferente.\n")
                                               print("\nSe Especula que se tardara en desocupar el sector en aproximadamente 1 Hora.")
                                               horario= True
                                        pos+=1
                

                                    if not horario:
                                           print ("\nSeguro qué quiere modificar la Hora?")
                                           print ("\n1_ Si")
                                           print("\n2_ No\n\n")
                                           a = input("Elija  una opción: ")
                
                                           if (a == "1"):
                                              print("\nLa nueva Hora de Inicio programada es : ",nueva_EntradaH)
                                              modificaHoraIni(encontrado,nueva_EntradaH)
                                              valido = True

                                           elif(a =="2"):
                                        
                                             print("\n\nRegresando al menú principal. \n")
                                             valido=True

                                           else:
                                             print("\n\n-------Vuelva a intentarlo.---------")
                                             if (hora_Actual >= datetime.strptime("23:00", "%H:%M").time()):
                                                 print("\n\nRegresando al menú principal. \n")
                                                 valido=True
                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")

                

                            elif(fecha_Anterior> fecha_Hoy):
                                
                                if(validar_Nuevo_Horario(nueva_EntradaH,hora_Anterior)):
                                    
                                    fechaNueva=datetime.strptime(verFechaP(encontrado), "%d/%m/%Y").date()
                                    nuevaHora= datetime.strptime(nueva_EntradaH, "%H:%M").time()
                                    inicioNuevo=datetime.combine(fechaNueva, nuevaHora)
                                    finNuevo=inicioNuevo+timedelta(hours=1)
                                    pos=0
                                    horario=False
                                    
                                    while pos <tamanio(o):
                                        b= recuperar(o,pos)
                                        if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == verFechaP(encontrado )):
                                           horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                           inicioExistente = datetime.combine(fechaNueva, horaExistente)
                                           finExistente= inicioExistente + timedelta(hours=1)

                                           if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                               print("\nHay una Máquina de este sector ya ha sido Asignados para este horario.\n\nCargue un Horario diferente.\n")
                                               print("\nSe Especula que se tardara en desocupar el sector en aproximadamente 1 Hora.")
                                               horario= True
                                        pos+=1
                

                                    if not horario:
                                           print ("\nSeguro qué quiere modificar la Hora?")
                                           print ("\n1_ Si")
                                           print("\n2_ No\n\n")
                                           a = input("Elija  una opción: ")
                
                                           if (a == "1"):
                                              print("\nLa nueva Hora de Inicio programada es : ",nueva_EntradaH)
                                              modificaHoraIni(encontrado,nueva_EntradaH)
                                              valido = True

                                           elif(a =="2"):
                                        
                                             print("\n\nRegresando al menú principal. \n")
                                             valido=True

                                           else:
                                             print("\n\n-------Vuelva a intentarlo.---------")
                                             if (hora_Actual >= datetime.strptime("23:00", "%H:%M").time()):
                                                 print("\n\nRegresando al menú principal. \n")
                                                 valido=True
                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")

                             
                     
                                
        
                    elif(mismamaq >1):
                        print("\n\nLa Máquina buscada contiene varias Horas asignadas.\n Elija la opción de Modificación por fecha y hora.\n")
                        valido = True    

                    else:
                        print ("\nNo se encontró ninguna orden identificada con ese ID de Máquina.\n")
                        valido= True

                        
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\n-------Regresando al Menu Principal.---------")
                    valido = True

        
          
         #pide id de la maquina y modifica fecha y hora, al ponerlos correctamente te pide confirmacion por si o por no y las guarda
        elif(opci=="3"):
            print("Modifica Fecha y Hora")
            print("\n---------------------------------------------------------------------------\n")
            valido = False
            if(tamanio(o)==0):
                print("\n\nNo se puede modificar la fecha/hora, si no hay Ordenes programadas.\n")
                valido=True
            while not valido:
                i=input("\nIngrese el Número ID de la Máquina que quiera identificar :")


                
                    
                if (validarNumerico(i)):
                    
                    buscado=(i)
                    encontrado = None

                    pos = 0

                    while pos < tamanio(o) and encontrado is None:
                        
                        b = recuperar(o,pos)
                
                        if verIDM(b) == buscado:
                            
                            encontrado= b
                        pos += 1
                
                    if encontrado:
                        print("Existe el Número ID de la Máquina. ")

                        print("-----------------------------------------------------------------------------\n")
                        valido = False 
                        while not valido:
                            fecha_Hoy = date.today()
                            fecha_Anterior_Str= verFechaP(encontrado)
                            fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()
                            
                            print("\nLa fecha programada anteriormente es : ",verFechaP(encontrado))
                            nueva_EntradaF= input(f"\n\nIngrese la Nueva Fecha Programada (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")


                            
                            if(validar_Nueva_Fecha(nueva_EntradaF, fecha_Hoy,fecha_Anterior)):
                                inicioNuevo=datetime.combine(datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(),datetime.strptime(verHoraIni(encontrado), "%H:%M").time())
                                finNuevo=inicioNuevo+timedelta(hours=1)
                                pos=0
                                horario=False
                    
                                while pos <tamanio(o):
                                    b= recuperar(o,pos)
                        
                                    if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == nueva_EntradaF):
                                        horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                        inicioExistente = datetime.combine (datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(), horaExistente)
                                        finExistente= inicioExistente + timedelta(hours=1)

                                        if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                            print("\nHay otra Máquina que ya tiene el horario asignado en esa Fecha.\n Cargue un Horario diferente.\n")
                                            horario= True
                                    pos+=1
                

                                if not horario:
                                    print ("\nSeguro qué quiere modificar la Fecha?")
                                    print ("\n1_ Si")
                                    print("\n2_ No\n\n")
                                    a = input("Elija  una opción: ")
                
                                    if (a == "1"):
                                        print("\n[Ingreso Correcto de La Nueva Fecha Programada.]")
                                        print("\nLa Nueva Fecha Programada es : ",nueva_EntradaF)
                                        modificaFecha(encontrado,nueva_EntradaF)
                                        valido = True

                                    elif(a =="2"):
                                        print("\n\nRegresando al menú principal. \n")
                                        valido=True

                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")
                          


                            else:
                                print("\n\n-------Vuelva a intentarlo.---------")
                            
                        

                        #opcion continua, pide que le ingreses una hora nueva para reprogramar, en caso de que el sector tenga alguna otra maquina trabajando ese dia y hora
                        #te pide que ingreses una opcion diferente
                        print("-----------------------------------------------------------------------------\n")
                        valido = False 
                        while not valido:
                                
#########  
                            hora_Actual = datetime.now().time()
                     
                            hora_Anterior_Str= verHoraIni(encontrado)
                            hora_Anterior=datetime.strptime(hora_Anterior_Str, "%H:%M").time()

                            print("\nLa Hora de inicio programada anteriormente es : ",verHoraIni(encontrado))
                     
                            nueva_EntradaH= input(f"\nIngrese la Nueva Hora de Inicio (HH:MM). Hora Actual es [{hora_Actual.strftime( '%H:%M')}]: ")

                            fecha_Hoy = date.today()
                            fecha_Anterior_Str= verFechaP(encontrado)
                            fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                            if (fecha_Anterior == fecha_Hoy):
                                
                                if(validar_Nueva_Hora(nueva_EntradaH, hora_Actual,hora_Anterior)):
                                    fechaNueva=datetime.strptime(verFechaP(encontrado), "%d/%m/%Y").date()
                                    nuevaHora= datetime.strptime(nueva_EntradaH, "%H:%M").time()
                                    inicioNuevo=datetime.combine(fechaNueva, nuevaHora)
                                    finNuevo=inicioNuevo+timedelta(hours=1)
                                    pos=0
                                    horario=False
                    
                                    while pos <tamanio(o):
                                        b= recuperar(o,pos)
                                        if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == verFechaP(encontrado )):
                                           horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                           inicioExistente = datetime.combine(fechaNueva, horaExistente)
                                           finExistente= inicioExistente + timedelta(hours=1)

                                           if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                               print("\nHay una Máquina de este sector ya ha sido Asignados para este horario.\n\nCargue un Horario diferente.\n")
                                               print("\nSe Especula que se tardara en desocupar el sector en aproximadamente 1 Hora.")
                                               horario= True
                                        pos+=1
                

                                    if not horario:
                                           print ("\nSeguro qué quiere modificar la Hora?")
                                           print ("\n1_ Si")
                                           print("\n2_ No\n\n")
                                           a = input("Elija  una opción: ")
                
                                           if (a == "1"):
                                              print("\nLa nueva Hora de Inicio programada es : ",nueva_EntradaH)
                                              modificaHoraIni(encontrado,nueva_EntradaH)
                                              valido = True

                                           elif(a =="2"):
                                        
                                             print("\n\nRegresando al menú principal. \n")
                                             valido=True

                                           else:
                                             print("\n\n-------Vuelva a intentarlo.---------")
                                             if (hora_Actual >= datetime.strptime("23:00", "%H:%M").time()):
                                                 print("\n\nRegresando al menú principal. \n")
                                                 valido=True
                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")

                

                            elif(fecha_Anterior> fecha_Hoy):
                                
                                if(validar_Nuevo_Horario(nueva_EntradaH,hora_Anterior)):
                                    
                                    fechaNueva=datetime.strptime(verFechaP(encontrado), "%d/%m/%Y").date()
                                    nuevaHora= datetime.strptime(nueva_EntradaH, "%H:%M").time()
                                    inicioNuevo=datetime.combine(fechaNueva, nuevaHora)
                                    finNuevo=inicioNuevo+timedelta(hours=1)
                                    pos=0
                                    horario=False
                                    
                                    while pos <tamanio(o):
                                        b= recuperar(o,pos)
                                        if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == verFechaP(encontrado )):
                                           horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                           inicioExistente = datetime.combine(fechaNueva, horaExistente)
                                           finExistente= inicioExistente + timedelta(hours=1)

                                           if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                               print("\nHay una Máquina de este sector ya ha sido Asignados para este horario.\n\nCargue un Horario diferente.\n")
                                               print("\nSe Especula que se tardara en desocupar el sector en aproximadamente 1 Hora.")
                                               horario= True
                                        pos+=1
                

                                    if not horario:
                                           print ("\nSeguro qué quiere modificar la Hora?")
                                           print ("\n1_ Si")
                                           print("\n2_ No\n\n")
                                           a = input("Elija  una opción: ")
                
                                           if (a == "1"):
                                              print("\nLa nueva Hora de Inicio programada es : ",nueva_EntradaH)
                                              modificaHoraIni(encontrado,nueva_EntradaH)
                                              valido = True

                                           elif(a =="2"):
                                        
                                             print("\n\nRegresando al menú principal. \n")
                                             valido=True

                                           else:
                                             print("\n\n-------Vuelva a intentarlo.---------")
                                             if (hora_Actual >= datetime.strptime("23:00", "%H:%M").time()):
                                                 print("\n\nRegresando al menú principal. \n")
                                                 valido=True
                                    else:
                                        print("\n\n-------Vuelva a intentarlo.---------")

                             
                        

                    else:
                        print ("\nNo se encontró ninguna orden identificada con ese ID de Máquina.\n")
                        valido= True

                        
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\n-------Regresando al Menu Principal.---------")
                    valido = True
                

           
          #regresa al menu principal

        elif (opci == "4"):
            print ("\n\n----Regresando al Menú Principal.------\n\n")
            
        else:
            print("Opción incorrecta.")
    

       #tercer submenú     
    elif (opcion =="3"):
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Cancelación de Tareas.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")

        print("-----Elija un método especifico para encontrar la orden de trabajo que desee eliminar----\n")

        print("1_  Búsqueda y Eliminación por ID de Máquina.\n")
        print("2_  Búsqueda y Eliminación por Fecha y Horario Programado.\n")
        print("3_  Búsqueda y Eliminación por Técnico Asignado.\n")
        print("4_  Regresar al menú principal. \n")
        opc=input("Elige una opción: ")
        justificacion1=0
        justificacion2=0
        #pregunta por el id de la maquina lo busca a través de eso y detecta la orden de trabajo, pide confirmacion y la elimina
        #pide una justificacion por la eliminacion de la orden a través de un submenú
        if (opc=="1"):
            
             print("Búsqueda y Eliminación por ID de Máquina.\n")
             print("\n---------------------------------------------------------------------------\n")
             
             valido = False
             if(tamanio(o) == 0):
                 print("\n\n No Hay ID de Máquina disponibles para Búscar y Eliminar. \n")
                 valido = True
             while not valido:
                i=input("\nIngrese el Número ID de la Máquina que quiera identificar :")
                
                if (validarNumerico(i)):
                    

                    buscado=(i)
                    encontrado = None

                    pos = 0
                    contador = 0
                    mismamaq=0
             
             
                    while pos < tamanio(o) :
                      b = recuperar(o,pos)
                
                      if verIDM(b) == buscado:
                          encontrado= b
                          contador=o
                          mismamaq += 1
                          print("\n\nOrden a ejecutar : ",(verOrden(b)))
                          print("\nDatos de la programación :\n")
                          print("\nTécnico Asignado: ",(verIDM(b)))
                          print("\nFecha Programada: ",(verFechaP(b)))
                          print("\nHora de Inicio: ",(verHoraIni(b)))
                          print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" ) 
                      
                      
                      pos += 1
                
                    if encontrado and mismamaq == 1:
                        
                 
                        print("\n\nNúmero ID de la Máquina: Encontrado. \n")
                        print("\nLa Orden dada es : ",verOrden(encontrado))
                        print("\nSeguro qué quiere Eliminar esta Orden?")
                        print("\n1_ Si")
                        print("\n2_ No\n\n")
                        a= input("Elija una opción: ")

                        if (a == "1"):
                            
                            eliminarDatosTecnicos(contador,encontrado)
                            print("Comprobación de Eliminación de la Orden")

                            pos= 0
                            while pos < tamanio(o) :
                                            
            
                                b = recuperar(o,pos)
            
                                print("\n\nOrden a ejecutar : ",(verOrden(b)))
                                print("\nDatos de la programación :\n")
                                print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                                print("\nNombre del Equipo: ",(verNomEquipo(b)))
                                print("\nTécnico Asignado: ",(verTecniAsi(b)))
                                print("\nSector de Planta: ",(verSectorP(b)))
                                print("\nFecha Programada: ",(verFechaP(b)))
                                print("\nHora de Inicio: ",(verHoraIni(b)))
                                print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                                pos += 1
                            print("\nProceso de eliminación completado. \n")

                            print("-----------------------------------------------------------------------------\n")


                            opcional=""
                            while opcional not in ["1" , "2"] :
                     
                                print ("Ingrese el motivo por el cual elimino la orden de trabajo del proceso de planificación: ")
                                print("1_  Falta de Respuestos.\n")
                                print("2_  Cambio en la prioridad de la planta.\n")
                                opcional= input("Elige una opción: ")

                                if(opcional=="1"):
                                    
                                    print("\n\nMotivo Ingresado: Falta de Respuestos.\n\n")
                                    justificacion1+= 1
                                    valido = True

                                elif(opcional=="2"):
                                    print("\n\nMotivo Ingresado: Cambio en la prioridad de la planta. \n\n")
                                    justificacion2+= 1
                                    valido = True
                                    
                                else:
                                    print("\n\nOpcion Invalida, Elige otra opción.\n")

                        elif(a == "2"):
                            
                            print("\n\nRegresando al Menú principal. \n")
                            valido = True

                        else:
                            
                            print("\n\n-------Vuelva a intentarlo.---------")


                    elif(encontrado and mismamaq >1):
                        print("\n\nLa Máquina buscada contiene varias ordenes asignadas.\n\nElija la opción : Búsqueda y Eliminación por Fecha y Horario Programado.\n")
                        valido = True
                    
                    else:
                        print ("\n\nNo se encontró ninguna orden identificada con ese ID de Máquina.\n\n")
                        valido = True

                
                    
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\n-------Regresando al Menu Principal.---------")
                    valido = True

            

             
         #pide ingresar una fecha y hora programada para detectar la existencia de esa orden trabajo, compara con las ya existentes, y si la encunetra pide confirmacion para eliminar
         #tambien pide una justificacion por medio de un submenu
        elif(opc=="2"):
            

            print("Búsqueda y Eliminación por Fecha y Horario Programado.\n")
            print("\n---------------------------------------------------------------------------\n")
            
            valido = False
            if(tamanio(o) == 0):
                 print("\n\n No Hay Fecha/Hora disponibles para Búscar y Eliminar. \n")
                 valido = True
            while not valido:
                
                fecha_Hoy = date.today()

                entradaF= input(f"\nIngrese la Fecha Programada que desea buscar (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")

                

                    
                if(validarFecha(entradaF, fecha_Hoy)):
                    print("[Ingreso Correcto de La Fecha Programada.]")
                    valido = True
                else:
                    print("\n\n-------Vuelva a intentarlo.---------")

            print("-----------------------------------------------------------------------------\n")
            valido = False
            if(tamanio(o) == 0):
                valido = True
            while not valido:

                hora_Actual = datetime.now().time()
                fecha_Anterior_Str = entradaF
                fecha_Anterior = datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                entradaH= input(f"\nIngrese la Hora de Inicio que desea Buscar (HH:MM). Hora Actual es [{hora_Actual.strftime('%H:%M')}]: ")
                if(fecha_Anterior == fecha_Hoy):
                    if(validarHora(entradaH, hora_Actual)):
                        
                        encontrado = None

                        pos=0
                        contador = 0
                        while pos< tamanio(o) and encontrado is None:

                            b = recuperar(o,pos)

                            if verFechaP(b) == entradaF and verHoraIni(b) == entradaH :
                                
                                encontrado = b
                                contador = o


                            pos += 1
                        if encontrado:
                            
                 
                            print("\n\nFecha y Hora programadas: Encontrado. \n")
                            print("\nLa Orden dada es : ",verOrden(encontrado))
                            print("\nSeguro qué quiere Eliminar esta Orden?")
                            print("\n1_ Si")
                            print("\n2_ No\n\n")
                            a= input("Elija una opción: ")

                            if (a == "1"):
                                
                                eliminarDatosTecnicos(contador,encontrado)
                                print("Comprobación de Eliminación de la Orden")

                                pos= 0
                                while pos < tamanio(o) :
                                    
                                    b = recuperar(o,pos)
            
                                    print("\n\nOrden a ejecutar : ",(verOrden(b)))
                                    print("\nDatos de la programación :\n")
                                    print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                                    print("\nNombre del Equipo: ",(verNomEquipo(b)))
                                    print("\nTécnico Asignado: ",(verTecniAsi(b)))
                                    print("\nSector de Planta: ",(verSectorP(b)))
                                    print("\nFecha Programada: ",(verFechaP(b)))
                                    print("\nHora de Inicio: ",(verHoraIni(b)))
                                    print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                                    pos += 1
                                print("\nProceso de eliminación completado. \n")

                                print("-----------------------------------------------------------------------------\n")

                                opcional=""
                                while opcional not in ["1" , "2"] :
                                    
                     
                                    print ("Ingrese el motivo por el cual elimino la orden de trabajo del proceso de planificación: ")
                                    print("1_  Falta de Respuestos.\n")
                                    print("2_  Cambio en la prioridad de la planta.\n")
                                    opcional= input("Elige una opción: ")

                                    if(opcional=="1"):
                                    
                                        print("\n\nMotivo Ingresado: Falta de Respuestos.\n\n")
                                        justificacion1+= 1
                                        valido = True

                                    elif(opcional=="2"):
                                        print("\n\nMotivo Ingresado: Cambio en la prioridad de la planta. \n\n")
                                        justificacion2+= 1
                                        valido = True
                                    
                                    else:
                                        print("\n\nOpcion Invalida, Elige otra opción.\n")

                            elif(a == "2"):

                            
                                print("\n\nRegresando al Menú principal. \n")
                                valido = True

                            else:
                                print("\n\n-------Vuelva a intentarlo.---------")
                 
                        else:
                            print("\n\nNo se encontró ninguna orden identificada con esa Fecha y Hora.\n\n")
                            valido = True
                            
                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                        valido = True

                elif(fecha_Anterior> fecha_Hoy):
                    
                    if(validarHorario(entradaH)):
                        
                    
                        encontrado = None

                        pos=0
                        contador = 0
                        while pos< tamanio(o) and encontrado is None:

                            b = recuperar(o,pos)

                            if verFechaP(b) == entradaF and verHoraIni(b) == entradaH :
                                encontrado = b
                                contador = o

                   

                            pos += 1
                        if encontrado:
                            
                            print("\n\nFecha y Hora programadas: Encontrado. \n")
                            print("\nLa Orden dada es : ",verOrden(encontrado))
                            print("\nSeguro qué quiere Eliminar esta Orden?")
                            print("\n1_ Si")
                            print("\n2_ No\n\n")
                            a= input("Elija una opción: ")

                            if (a == "1"):
                            
                                eliminarDatosTecnicos(contador,encontrado)
                                print("Comprobación de Eliminación de la Orden")

                                pos= 0
                                while pos < tamanio(o) :
                                
                                    b = recuperar(o,pos)
            
                                    print("\n\nOrden a ejecutar : ",(verOrden(b)))
                                    print("\nDatos de la programación :\n")
                                    print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                                    print("\nNombre del Equipo: ",(verNomEquipo(b)))
                                    print("\nTécnico Asignado: ",(verTecniAsi(b)))
                                    print("\nSector de Planta: ",(verSectorP(b)))
                                    print("\nFecha Programada: ",(verFechaP(b)))
                                    print("\nHora de Inicio: ",(verHoraIni(b)))
                                    print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                                    pos += 1
                                print("\nProceso de eliminación completado. \n")

                                print("-----------------------------------------------------------------------------\n")

                                opcional=""
                                while opcional not in ["1" , "2"] :
                                
                                    print ("Ingrese el motivo por el cual elimino la orden de trabajo del proceso de planificación: ")
                                    print("1_  Falta de Respuestos.\n")
                                    print("2_  Cambio en la prioridad de la planta.\n")
                                    opcional= input("Elige una opción: ")

                                    if(opcional=="1"):
                                    
                                        print("\n\nMotivo Ingresado: Falta de Respuestos.\n\n")
                                        justificacion1+= 1
                                        valido = True

                                    elif(opcional=="2"):
                                    
                                        print("\n\nMotivo Ingresado: Cambio en la prioridad de la planta. \n\n")
                                        justificacion2+= 1
                                        valido = True
                                    
                                    else:
                                        print("\n\nOpcion Invalida, Elige otra opción.\n")

                            elif(a == "2"):

                                print("\n\nRegresando al Menú principal. \n")
                                valido = True

                            else:
                                print("\n\n-------Vuelva a intentarlo.---------")
                 
                        else:
                            print("\n\nNo se encontró ninguna orden identificada con esa Fecha y Hora.\n\n")
                            valido=True
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\n-------Regresando al Menu Principal.---------")
                    valido = True
        
#prueba de opcion 2 reparada, fuerza una salida cuando no coincide
            

        #pide que ingreses un tecnico, compara con uno ya existente, si lo encuentra entonces pide confirmacion para eliminar la orden y tambien pide justificacion a traves del submenú
        elif(opc=="3"):
            
             print("Búsqueda y Eliminación por Técnico Asignado.\n")
             print("\n---------------------------------------------------------------------------\n")
             
             valido = False
             if(tamanio (o) == 0):
                 print("\n\n No Hay Técnico Asignado disponibles para Búscar y Eliminar. \n")
                 valido = True
             while not valido:
                i=normalizar_mayus(input("\nIngrese el Técnico Asignado que quiera identificar :"))
            
                if (validarTexto(i)):
                    buscado=(i)
                    encontrado = None

                    pos = 0
                    contador=0
                    mismotecnico=0
                    while pos < tamanio(o) :
                        b = recuperar(o,pos)
                
                        if verTecniAsi(b) == buscado:
                            encontrado = b
                            contador = o
                            mismotecnico+=1
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" ) 
                      
                        pos += 1
                
                    if encontrado and mismotecnico == 1:
                        print("\n\nTécnico Asignado: Encontrado. \n")
                        print("\n\nOrden a ejecutar : ",(verOrden(b)))
                        print("\nSeguro qué quiere Eliminar esta Orden?")
                        print("\n1_ Si")
                        print("\n2_ No\n\n")
                        a= input("Elija una opción: ")

                        if (a == "1"):
                            eliminarDatosTecnicos(contador,encontrado)
                            print("Comprobación de Eliminación de la Orden")

                            pos= 0
                            while pos < tamanio(o) :
                                b = recuperar(o,pos)
            
                                print("\n\nOrden a ejecutar : ",(verOrden(b)))
                                print("\nDatos de la programación :\n")
                                print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                                print("\nNombre del Equipo: ",(verNomEquipo(b)))
                                print("\nTécnico Asignado: ",(verTecniAsi(b)))
                                print("\nSector de Planta: ",(verSectorP(b)))
                                print("\nFecha Programada: ",(verFechaP(b)))
                                print("\nHora de Inicio: ",(verHoraIni(b)))
                                print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                                pos += 1
                            print("\nProceso de eliminación completado. \n")

                            print("-----------------------------------------------------------------------------\n")
                     


                            opcional=""
                            while opcional not in ["1" , "2"] :
                                print ("Ingrese el motivo por el cual elimino la orden de trabajo del proceso de planificación: ")
                                print("1_  Falta de Respuestos.\n")
                                print("2_  Cambio en la prioridad de la planta.\n")
                                opcional= input("Elige una opción: ")

                                if(opcional=="1"):
                                    print("\n\nMotivo Ingresado: Falta de Respuestos.\n\n")
                                    justificacion1+= 1
                                    valido = True

                                elif(opcional=="2"):
                                    print("\n\nMotivo Ingresado: Cambio en la prioridad de la planta. \n\n")
                                    justificacion2+= 1
                                    valido = True
                                else:
                                    print("\n\nOpcion Invalida, Elige otra opción.\n")

                        elif(a == "2"):
                            print("\n\nRegresando al Menú principal. \n")
                            valido = True

                        else:
                            print("\n\n-------Vuelva a intentarlo.---------")
                    
                    elif(mismotecnico > 1):
                        print("\n\nEl Técnico Asignado contiene varias ordenes asignadas.\n\nElija la opción : Búsqueda y Eliminación por Fecha y Horario Programado.\n")
                        valido = True
                    elif(tamanio(o)>0):
                        print ("\n\nNo se encontró ninguna orden identificada con ese Técnico Asignado.\n\n")
                        print("\n\n-------Vuelva a intentarlo.---------")
                    
                    else:
                        print("\n\n-------Regresando al Menu Principal.---------")
                        valido = True
                else:
                    print("\n\n-------Vuelva a intentarlo.---------")
                    valido = True

             
                 
        elif(opc=="4"):
            print ("\n\n----Regresando al Menú Principal.------\n\n")


        else:
        
            print("\n\nOpción incorrecta.\n\n")
            
            
        #reporte general de mantenimiento simplemente muestra las ordenes vigentes y los datos de cada una
    elif (opcion =="4"):
        if ( tamanio (o) > 0 ):
            print("/////////////////////////////////////////////////////////////////////////////\n\n")
            print("Reporte General de Mantenimiento.\n")
            print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
            print("\n---------------------------------------------------------------------------\n")
            print("-----------------------------------------------------------------------------\n")

            print("-----Muestra de órdenes de trabajo almacenadas----\n")
            pos = 0 
            while pos < tamanio(o):
                b = recuperar(o,pos)
            
                print("\n\nOrden a ejecutar : ",(verOrden(b)))
                print("\nDatos de la programación :\n")
                print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                print("\nNombre del Equipo: ",(verNomEquipo(b)))
                print("\nTécnico Asignado: ",(verTecniAsi(b)))
                print("\nSector de Planta: ",(verSectorP(b)))
                print("\nFecha Programada: ",(verFechaP(b)))
                print("\nHora de Inicio: ",(verHoraIni(b)))
                print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                pos += 1
        else:
            print("\n\n-----No hay órdenes de trabajo almacenadas----\n")

        #funcional
#reprograma la fechas de todas las ordenes, que pertenezcan a esa fecha elegida y modifica las mismas
    elif(opcion == "5"):
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Reprogramación por Parada de Planta.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")

        

        
        print("Búsqueda de fecha para reprogramar órdenes de trabajo.\n")
        
        valido = False
        if(tamanio (o) == 0):
                 print("\n\n No Hay Ordenes asignadas para Reprogramar. \n")
                 valido = True
        while not valido:
            
                
            fecha_Hoy = date.today()

            pos=0
            while pos < tamanio(o):
                b = recuperar(o,pos)
                         
                print("\n\nOrden a ejecutar : ",(verOrden(b)))
                print("\nDatos de la programación :\n")
                print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                print("\nNombre del Equipo: ",(verNomEquipo(b)))
                print("\nTécnico Asignado: ",(verTecniAsi(b)))
                print("\nSector de Planta: ",(verSectorP(b)))
                print("\nFecha Programada: ",(verFechaP(b)))
                print("\nHora de Inicio: ",(verHoraIni(b)))
                print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                pos += 1

            entradaF= input(f"\nIngrese la Fecha Programada que desea buscar (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")
             
            if(validarFecha(entradaF, fecha_Hoy)):

                buscado=(entradaF)
                encontrado = None

                pos = 0
             
             
                while pos < tamanio(o):
                    
                    b = recuperar(o,pos)
                
                    if verFechaP(b) == buscado:
                        encontrado = b
                        
                      
                    pos += 1
                if(encontrado):
                    print("\nFecha Existe.\n")
                    fecha_Anterior_Str= verFechaP(encontrado)
                    fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                    print("-----------------------------------------------------------------------------\n")
                    validacion = False
                    while not validacion:
                        
                        fecha_Hoy = date.today()
 
                        nueva_EntradaF= input(f"\nIngrese la Fecha de Reprogramación de todas las ordenes encontradas (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")
                     
                        if(validar_Nueva_Fecha(nueva_EntradaF, fecha_Hoy,fecha_Anterior)):
                            if encontrado is not None:
                                
                                inicioNuevo= datetime.combine(datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(),datetime.strptime(verHoraIni(encontrado), "%H:%M").time())

                                finNuevo=inicioNuevo+timedelta(hours=1)
                            else:
                                print("\nNo se encontró ninguna orden para esa fecha.\n")
                            pos=0
                            horario=False
                    
                            while pos <tamanio(o):
                                b= recuperar(o,pos)
                        
                                if(verSectorP(b) == verSectorP(encontrado) and verFechaP(b) == nueva_EntradaF):
                                    
                                    horaExistente = datetime.strptime(verHoraIni(b), "%H:%M").time()
                                    inicioExistente = datetime.combine (datetime.strptime(nueva_EntradaF, "%d/%m/%Y").date(), horaExistente)
                                    finExistente= inicioExistente + timedelta(hours=1)

                                    if not(finNuevo <= inicioExistente or inicioNuevo >= finExistente):
                                        
                                        print("\nNo se puede reprogramar en esa Fecha, hay otras máquinas asignadas para ese sector,fecha y horario.\nIntente con una Fecha diferente.\n")
                                        horario= True
                                pos+=1
                
###########################################################################################
                            if not horario:
                                
                                encontrado = None

                                pos=0
                                reprogramacion=False

                                while pos< tamanio(o):
                                    
                                    b = recuperar(o,pos)

                                    if verFechaP(b) == entradaF :
                                        
                                        reprogramacion=True

                                    pos += 1
                                if reprogramacion:
                                    
                                    print ("\nSeguro que quiere Reprogramar las fechas de estas ordenes?")
                                    print ("\n1_ Si")
                                    print("\n2_ No\n\n")
                                    a = input("Elija  una opción: ")
                
                                    if (a == "1"):
                                        
                                        encontrado = None
                                        pos=0
                                        while pos<tamanio(o):
                                            
                                            b = recuperar(o,pos)

                                            if verFechaP(b)== entradaF:
                                                
                                                encontrado = b
                                                modificaFecha(encontrado,nueva_EntradaF)
                                            pos+=1
                                        print("Comprobación de Las Reprogramaciones Realizadas")

                                        pos=0
                                        while pos < tamanio(o):
                                            b = recuperar(o,pos)
                         
                                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                                            print("\nDatos de la programación :\n")
                                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                                            print("\nSector de Planta: ",(verSectorP(b)))
                                            print("\nFecha Programada: ",(verFechaP(b)))
                                            print("\nHora de Inicio: ",(verHoraIni(b)))
                                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                                            pos += 1
                                        print("\n\n[Reprogramación realizada con exito].\n")
                                        valido = True
                                        validacion = True


                                    elif(a =="2"):
                                        
                                        print("\n\nRegresando al menú principal. \n")
                                        valido = True
                                        validacion=True

                                    else:
                                        print("\n\n-------Opción Invalida.---------")
            
                
                        else:
                            print("\n\n-------Vuelva a intentarlo.---------")

                else:
                    print("\nLa fecha ingresada no es válida.\n\n")
                    print("\n\n-------Vuelva a intentarlo.---------")

            else:
                print("\n\n-------Vuelva a intentarlo.---------")


        #opcion 6, sale un sub menu y te pide elegir entre 4 posibilidades, dependiendo la que elijas te da la opcion de eliminar entre todos los sectores disponibles.
        #o generar una cola, también esta la opcion de hacer los dos al mismo tiempo o regresar al menu principal
    elif(opcion == "6"):
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Depuración y Generación de Lista de Prioridad.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")

        

        
        print("-----Submenú----\n")

        print("1_  Dar de Baja por Sector.\n")
        print("2_  Generar cola de intervención.\n")
        print("3_  Dar de Baja por Sector y Generar cola de intervención.\n")
        print("4_  Regresar al menú principal. \n")
        sub=input("Elige una opción: ")

        if (sub == "1"):
            print("\n\n  Dar de Baja por Sector.\n")
            print("-----------------------------------------------------------------------------\n")
            valido=False
            while not valido:
                
                print("\n Elija el Sector de la Planta para Eliminar todas las órdenes de trabajo asociadas : \n")
                print("1_  Producción.\n")
                print("2_  Embalaje.\n")
                print("3_  Fundición.\n")
                print("4_  Deposito.\n")
                print("5_  Regresar al Menú Principal. \n")

            
                se=input("\nIngrese el Sector de la Planta :")

                if(se == "1" and tamanio(o) > 0):
                    print("\n\n[Sector de la Planta: Producción.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector? ")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        
                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)
                            a = verSectorP(b)

                            if verSectorP(b)== "Producción": 
                                
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        print("\n\nRegresando al Menú principal. \n")
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                    

                elif(se == "2" and tamanio(o) > 0):
                    print("\n\n[Sector de la Planta: Embalaje.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):
                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Embalaje":
                                
                                eliminarDatosTecnicos(o,b)

                            else:
                                pos+=1
                        
                            
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        print("\n\nRegresando al Menú principal. \n")
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                        

                elif(se == "3" and tamanio(o) > 0):
                    print("\n\n[Sector de la Planta: Fundición.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Fundición":
                        
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        print("\n\nRegresando al Menú principal. \n")
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                    

                elif(se == "4" and tamanio(o) > 0):
                    print("\n\n[Sector de la Planta: Deposito.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Deposito":
                                
                                
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        print("\n\nRegresando al Menú principal. \n")
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                
                elif(se == "5" and tamanio(o) > 0):
                    print("\n\nRegresando al Menú principal. \n")
                    valido = True
                    
                elif(tamanio(o) == 0):
                    print("\n\nNo hay Sectores para Eliminar.\n")
                    valido = True
                else:
                    print("\n\n-------Vuelva a intentarlo.---------")

        elif(sub=="2"):
            print("\n\n  Generar cola de intervención.\n")
            print("-----------------------------------------------------------------------------\n")

            print("Búsqueda de fecha para generar la cola de intervención.\n")
        
            valido = False
            while not valido:
            
                pos=0
                while pos < tamanio(o):
                    b = recuperar(o,pos)
                         
                    print("\n\nOrden a ejecutar : ",(verOrden(b)))
                    print("\nDatos de la programación :\n")
                    print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                    print("\nNombre del Equipo: ",(verNomEquipo(b)))
                    print("\nTécnico Asignado: ",(verTecniAsi(b)))
                    print("\nSector de Planta: ",(verSectorP(b)))
                    print("\nFecha Programada: ",(verFechaP(b)))
                    print("\nHora de Inicio: ",(verHoraIni(b)))
                    print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                    pos += 1
                
                fecha_Hoy = date.today()

                entradaF= input(f"\nIngrese la Fecha Programada que desea buscar (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")
             
                if(validarFecha(entradaF, fecha_Hoy)):

                    buscado=(entradaF)
                    encontrado = None

                    pos = 0
                    contador=0
             
             
                    while pos < tamanio(o) and encontrado is None:
                    
                        b = recuperar(o,pos)
                
                        if verFechaP(b) == buscado:
                            encontrado = b
                            contador = o
                      
                        pos += 1
                    if(encontrado):
                        print("\nFecha Existe.\n")
                        fecha_Anterior_Str= verFechaP(encontrado)
                        fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                        print("\nSeguro qué quiere generar una cola de Intervención? ")
                        print("\n1_ Si")
                        print("\n2_ No\n\n")
                        a= input("Elija una opción: ")
                        if(a == "1"):
                            c=crearCola()
            
                            pos=0
            
                            while pos<tamanio(o) :
                                b = recuperar(o,pos)

                                if verFechaP(b) == buscado:
                                    equipo = verNomEquipo(b) 
                                    tecnico = verTecniAsi(b)
                                    encolar(c,(equipo,tecnico))
                                pos+=1
                            print("\n\nOrden de salida de los técnicos del taller. ")
                            pos=0
                            while not esVacia(c):
                                equipo,tecnico= desencolar(c)
                                pos +=1

                                print("\n\n",pos,"\n\nEquipo : ",equipo)
                                print("Técnico Asignado: ",tecnico)
                    
                                print("\n\n[Salida de los técnicos completada].")
                                valido = True

                        elif(a == "2"):
                
                            print("\n\nRegresando al Menú principal. \n")
                            valido = True
                        else:
                            print("\n\n-------Vuelva a intentarlo.---------")

                    else:
                        print ("\nNo se ha encontrado esa Fecha. \n\n")
                        print("\n\n-------Regresando al Menú Principal.---------")
                        valido = True
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\nNo hay Tecnicos para generar una cola.\n")
                    valido= True
            
            
        elif(sub=="3"):
            
            print("\n\n  Dar de Baja por Sector y Generación de cola de intervención.\n")
            print("-----------------------------------------------------------------------------\n")
            valido=False
            while not valido:
                print("\n\n  Dar de Baja por Sector.\n")
                print("\n Elija el Sector de la Planta para Eliminar todas las órdenes de trabajo asociadas : \n")
                print("1_  Producción.\n")
                print("2_  Embalaje.\n")
                print("3_  Fundición.\n")
                print("4_  Deposito.\n")
                print("5_  Regresar al Menú Principal. \n")

            
                se=input("\nIngrese el Sector de la Planta :")

                if(se == "1"):
                    print("\n\n[Sector de la Planta: Producción.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector? ")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Producción":
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                    

                elif(se == "2"):
                    print("\n\n[Sector de la Planta: Embalaje.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Embalaje":
                                
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                        

                elif(se == "3"):
                    print("\n\n[Sector de la Planta: Fundición.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Fundición":
                                
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                    

                elif(se == "4"):
                    print("\n\n[Sector de la Planta: Deposito.]\n")
                    print("\nSeguro qué quiere Eliminar las ordenes asociadas a este Sector?")
                    print("\n1_ Si")
                    print("\n2_ No\n\n")
                    a= input("Elija una opción: ")
                    if(a == "1"):

                        
                        pos=0
                        while pos<tamanio(o):
                            b = recuperar(o,pos)

                            if verSectorP(b)== "Deposito":
                                
                                eliminarDatosTecnicos(o,b)
                        
                            else:
                                pos+=1
                        
                        print("Comprobación de Las órdenes asociadas a el Sector de Planta. ")

                        pos=0
                        while pos < tamanio(o):
                            b = recuperar(o,pos)
                         
                            print("\n\nOrden a ejecutar : ",(verOrden(b)))
                            print("\nDatos de la programación :\n")
                            print("\nNúmero de ID de Máquinaria: ",(verIDM(b)))
                            print("\nNombre del Equipo: ",(verNomEquipo(b)))
                            print("\nTécnico Asignado: ",(verTecniAsi(b)))
                            print("\nSector de Planta: ",(verSectorP(b)))
                            print("\nFecha Programada: ",(verFechaP(b)))
                            print("\nHora de Inicio: ",(verHoraIni(b)))
                            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )         
                            pos += 1
                        print("\n\n[Eliminación de órdenes asociadas a el Sector de Planta realizada con exito].\n")
                        valido = True

                    elif(a== "2"):
                        valido = True

                    else:
                        print("\n\n-------Vuelva a intentarlo.---------")
                elif(se == "5"):
                    valido = True

                else:
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
            if ( (se == "1"and a == "1" or se == "2" and a == "1" or  se == "3" and a == "1" or se == "4"and a == "1")and tamanio(o)>0):
                print("\n\n  Generar cola de intervención.\n")
                print("-----------------------------------------------------------------------------\n")

                print("Búsqueda de fecha para generar la cola de intervención.\n")
        
            valido = False
            if (se == "5" or a == "2" or tamanio(o) == 0):
                if (tamanio(o) == 0):
                    print("\nNo se puede generar una Cola, si no hay Tecnicos. \n")
                print("\n\nRegresando al Menú principal. \n")
                valido = True
            while not valido :
            
                
                fecha_Hoy = date.today()

                entradaF= input(f"\nIngrese la Fecha Programada que desea buscar (DD/MM/AAAA). Hoy es {fecha_Hoy.day}/{fecha_Hoy.month}/{fecha_Hoy.year}: ")
             
                if(validarFecha(entradaF, fecha_Hoy)):

                    buscado=(entradaF)
                    encontrado = None

                    pos = 0
                    contador=0
             
             
                    while pos < tamanio(o) and encontrado is None:
                    
                        b = recuperar(o,pos)
                
                        if verFechaP(b) == buscado:
                            encontrado = b
                            contador = o
                      
                        pos += 1
                    if(encontrado):
                        print("\nFecha Existe.\n")
                        fecha_Anterior_Str= verFechaP(encontrado)
                        fecha_Anterior=datetime.strptime(fecha_Anterior_Str, "%d/%m/%Y").date()

                        print("\nSeguro qué quiere generar una cola de Intervención? ")
                        print("\n1_ Si")
                        print("\n2_ No\n\n")
                        a= input("Elija una opción: ")
                        if(a == "1"):
                            c=crearCola()
            
                            pos=0
            
                            while pos<tamanio(o) :
                                b = recuperar(o,pos)

                                if verFechaP(b) == buscado:
                                    equipo = verNomEquipo(b) 
                                    tecnico = verTecniAsi(b)
                                    encolar(c,(equipo,tecnico))
                                pos+=1
                            print("\n\nOrden de salida de los técnicos del taller. ")
                            pos=0
                            while not esVacia(c):
                                equipo,tecnico= desencolar(c)
                                pos +=1

                                print("\n\n",pos,"\n\nEquipo : ",equipo)
                                print("Técnico Asignado: ",tecnico)
                    
                                print("\n\n[Salida de los técnicos completada].")
                                valido = True

                        elif(a == "2"):
                
                            print("\n\nRegresando al Menú principal. \n")
                            valido = True
                        else:
                            print("\n\n-------Vuelva a intentarlo.---------")

                    else:
                        print ("\nNo se ha encontrado esa Fecha. \n\n")
                        print("\n\n-------Regresando al Menú Principal.---------")
                        valido = True
                elif(tamanio(o)>0):
                    print("\n\n-------Vuelva a intentarlo.---------")
                    
                else:
                    print("\n\nNo hay Tecnicos para generar una cola.\n")
                    valido= True         

        elif(sub == "4"):
            print("\n\nRegresando al Menú principal. \n")
            

        else:
            print("Opcion invalida.")
    #muestra todos los nombres de todas las ordenes vigentes.       
    elif(opcion == "7"):
        print("/////////////////////////////////////////////////////////////////////////////\n\n")
        print("Mostrar todas las órdenes vigentes.\n")
        print("/////////////////////////////////////////////////////////////////////////////\n\n")

        
        print("\n---------------------------------------------------------------------------\n")
        print("-----------------------------------------------------------------------------\n")
        pos=0
        contador=0
        while pos < tamanio(o):
            
            b = recuperar(o,pos)
            contador+=1
            
            print(contador,"_ Orden a ejecutar : ",(verOrden(b)))
            print ("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - \n" )
            print("\n")
            
            pos+=1
        if tamanio(o) == 0:
            print("No hay ordenes vigentes para mostrar. \n")

        

    
            
    #finaliza el programa    
    elif(opcion == "8"):
        print("\n Programa finalizado.\n")

    #da mensaje y vuelve al bucle    
    else:
        print("Opcion Invalida, Elige otra opción.\n")

