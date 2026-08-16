//Enunciado:

/*Una clínica mantiene un listado ordenado por código interno de cada paciente que fue atendido allí 
alguna vez, de los cuales se mantiene la siguiente información: 
1) Código interno. 
2) DNI. 
3) Nombre. 
4) Teléfono. 
5) Resumen historia clínica. 
6) Fecha primer ingreso. 
7) Fecha última atención. 
8) Ultimo diagnóstico médico.
9) Fecha última internación. 
 Cuando una persona se va a hacer atender, 
se presenta, pide número y espera a ser llamado. Si la persona es paciente, solo informa su DNI, 
de lo contrario provee toda su información personal requerida por el listado histórico de pacientes y se
encola en la cola de atención. Una vez recibidos todos los pacientes comienza la atención médica. 
El médico que atiende a un paciente actualiza la información correspondiente en el listado. 
Si un paciente requiere hacerse un análisis es colocado en una COLA DE ANALISIS, 
incluyendo la siguiente información: 1) DNI. 2) Diagnóstico. 3) Análisis requerido. 
4) Cantidad de estudios por imágenes simples. 5) Cantidad de estudios por imágenes complejas. 

Al finalizar el día, se requiere saber la cantidad de estudios por imágenes simples y complejas 
fueron ordenados recorriendo la cola recursivamente.

Desarrolle un algoritmo que realice el registro diario de la operatoria descripta emulando 
el proceso completo y obtenga cada uno de los puntos requeridos.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//registros 

typedef struct tipo_Paciente{
	int Codigo;
	int Dni;
	char Nombre[10];
	char Resumen[200];
	int Telefono;
	//fecha de ingreso 
	int primerafecha;
	//ultima fecha de atencion
	int ultimafecha;
	char anal[20];
	char diagnostico[200];
	//fecha de ultima internacion
	int ultimainternacion;
	int imagenes_simples,imagenes_complejas;
}paciente;

typedef struct tipo_nodo{
	paciente r;
	struct tipo_nodo *sig;
}nodo;

typedef struct tipo_cola{
	nodo *primero, *ultimo;
}t_cola;

//funciones prototipo 

void crear_lista(nodo **lista);//crea la lista
void crear_cola(t_cola *cola);//crea una cola
void cargar_paciente(paciente *re,int dni);//carga los datos de los pacientes
nodo *insertar_ordenado(nodo **lista,int dni);//inserta un paciente a la lista
nodo *buscar_valor(nodo *lista, int dni);//buscar un paciente
int lista_vacia(nodo *lista);//identifica si la lista esta vacia
void atender_paciente_recepcion(nodo **lista);
void encolar(t_cola *cola, nodo *p);
int cola_vacia(t_cola cola);
nodo *desencolar(t_cola *cola);
void atender_paciente(nodo *pac,t_cola *cola_analisis);
void recursivo(t_cola cola_analisis,int *imagenes_simples, int *imagenes_complejas);

int main (){
	system("color 0C");
	//declaracion de variables
	nodo *lista,*elemento;
	t_cola cola, cola_analisis;
	int imagenes_simples,imagenes_complejas;
	int dni,atencion=1;
	
	//inicializando
	crear_lista(&lista);
	crear_cola(&cola);
	crear_cola(&cola_analisis);
	atender_paciente_recepcion(&lista);
   
    
    while(atencion!=0){
    	printf ("Ingrese el dni: \n");
    	scanf("%d",&dni);
    	elemento= buscar_valor(lista,dni);
    	if(elemento==NULL){
    		elemento= insertar_ordenado(&lista,dni);
    		encolar(&cola,elemento);
    		printf ("Indique si hay mas pacientes?\n");
    		scanf ("%d",&atencion);
		}
	}
	
	while(!cola_vacia(cola)){
		elemento=desencolar(&cola);
		atender_paciente(elemento,&cola_analisis);
		
	}
	recursivo(cola,&imagenes_simples,&imagenes_complejas);
	
	printf ("la cantidad de imagenes por analisis simple es %d.\n",imagenes_simples);
	printf ("La cantidad de imagenes por analisis complejo es %d.\n",imagenes_complejas);
	
	system ("pause");
	return 0;	
}

//definicion de funciones
void crear_lista(nodo **lista){*lista=NULL;}

void crear_cola(t_cola *cola){
	cola->primero=NULL;
	cola->ultimo=NULL;
}

/*1) Código interno. 
2) DNI. 
3) Nombre. 
4) Teléfono. 
5) Resumen historia clínica. 
6) Fecha primer ingreso. 
7) Fecha última atención. 
8) Ultimo diagnóstico médico.
9) Fecha última internación.*/
 
void cargar_paciente(paciente *re,int dni){
	printf ("Cargue los datos del paciente: \n");
	printf ("INSERTE EL CODIGO INTERNO : \n");
	scanf ("%d",&re->Codigo);
	printf ("INGRESE EL DNI : \n");
	scanf ("%d",&re->Dni);
	printf ("ESCRIBA EL NOMBRE: \n");
	scanf ("%s",&re->Nombre);
	printf ("ANOTE EL NUMERO DE TELEFONO \n");
	scanf ("%d",&re->Telefono);
	printf("TRANSCRIBA EL RESUMEN DEL HISTORIAL CLINICO DEL PACIENTE: \n");
	scanf ("%s",&re->Resumen);
	printf ("PRIMERA FECHA DE INGRESO INGRESE DIA,MES Y ANO: \n");
	scanf ("%d",&re->primerafecha);
	printf ("ULTIMA FECHA DE INGRESO INGRESE DIA, MES Y ANO: \n");
	scanf("%d",re->ultimafecha);
	printf ("ESCRIBA EL ULTIMO DIAGNOSTICO MEDICO: \n");
	scanf ("%s",re->diagnostico);
	printf ("INGRESE LA ULTIMA VEZ QUE SE INTERNO. \n");
	scanf("%d",re->ultimainternacion);
	printf ("Registro completo. \n");
	strcpy(re->anal, "");
	re->imagenes_simples=0;
	re->imagenes_complejas=0;
	re->Dni=dni;
}

nodo *insertar_ordenado(nodo **lista, int dni){
	paciente re;
	nodo *actual, *anterior;
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	cargar_paciente(&re,dni);
	nuevo->r=re;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->r.Codigo<re.Codigo){
		anterior=actual;
		actual=actual->sig;
	}
	if(anterior!=NULL){	/*Inserto en el cuerpo*/
		anterior->sig=nuevo;
		nuevo->sig=actual;
	}else{				/*Inserto al inicio*/
		nuevo->sig=*lista;
		*lista=nuevo;
	}
	return nuevo;
}

nodo *buscar_valor(nodo *lista, int dni){
	nodo *aux;
	aux=lista;
	while(aux!=NULL && aux->r.Dni!=dni)
		aux=aux->sig;
	return aux;
}

int lista_vacia(nodo *lista){
	if(lista==NULL)
		return 1;
	else
		return 0;
}

void atender_paciente_recepcion(nodo **lista){
	int dni;
	printf ("Ingrese el dni del paciente (0 para terminar): \n");
	scanf ("%d",&dni);
	
	
	while (dni){
		insertar_ordenado(lista,dni);
		printf ("Ingrese el dni (0 para terminar):  \n");
		scanf ("%d",&dni);
		
	}
}

//ENCOLAR UN ELEMENTO
void encolar(t_cola *cola, nodo *p){
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->r=p->r;
	nuevo->sig=NULL;
	if(cola->primero==NULL){
		cola->primero=nuevo;
		cola->ultimo=nuevo;
	}else{
		cola->ultimo->sig=nuevo;
		cola->ultimo=nuevo;
	}
}
int cola_vacia(t_cola cola){
	if(cola.primero==NULL)
		return 1;
	else
		return 0;
}

nodo *desencolar(t_cola *cola){
	
	nodo *aux;
	aux=cola->primero;
	cola->primero=aux->sig;
	free(aux);
	return aux;
}

void atender_paciente(nodo *pac,t_cola *cola_analisis){
	int analisis;
	printf ("Ingrese la fecha: \n");
	scanf("%d",pac->r.primerafecha);
	printf("Escriba el diagnostico. \n");
	scanf("%s",pac->r.diagnostico);
	printf("Actualice el historial clinico. \n");
	scanf("s",pac->r.Resumen);
	printf("Indique si requiere analisis por imagen. \n");
	scanf("%d",&analisis);
	if(analisis){
		printf ("Ingrese la cantidad de imagenes simples. \n");
		scanf("%d",&pac->r.imagenes_simples);
		printf("Ingrese la cantidad de imagenes complejas. \n");
		scanf("%d",&pac->r.imagenes_complejas);
		encolar(cola_analisis,pac);
	}
		
	}

void recursivo(t_cola cola_analisis,int *imagenes_simples, int *imagenes_complejas){
	nodo *pac;
	if(!cola_vacia(cola_analisis)){
		pac=desencolar(&cola_analisis);
		*imagenes_simples= *imagenes_simples + pac->r.imagenes_simples;
		*imagenes_complejas= *imagenes_complejas + pac->r.imagenes_complejas;
		recursivo(cola_analisis,imagenes_simples,imagenes_complejas);
	}
}



