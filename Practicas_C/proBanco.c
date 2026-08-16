//Enunciado:

/*Un Banco atiende a sus clientes de 10 a 15 horas. El proceso de atención al público 
tiene cierta particularidad por la limitación de espacio físico que existe de tal forma que 
se atienden a los clientes por "turnos", haciendo ingresar a todos los clientes que aguardan 
afuera del local hasta un máximo de 25, a los que se los ordenará en la recepción para 
su posterior atención. La forma de ordenarlos es a través de una cola. El proceso de atención 
a clientes en cada "turno" es el siguiente: 
1) Existe una lista ordenada con los datos de todos los clientes que alguna vez fueron 
atendidos en el lugar. 
2) Los datos que mantiene la lista de los clientes son los siguientes: 
nombre, teléfono, número de documento y cantidad de veces atendido hasta el momento. 
3) La lista se mantiene ordenada por número de documento. 
4) A medida que ingresan los clientes, el recepcionista le pide el documento y se verifica 
si está registrado (si ya está en la lista de clientes). 
5) Si el cliente ya estaba registrado, entonces se incrementa en uno la cantidad de veces que 
fue atendido en el mes. 
6) Si no está registrado, se le pide el resto de los datos y se lo registra en el momento. 
7) Se encola para su posterior atención en una cola común. 
8) Para atender a los clientes hay 5 empleados que van llamando a los clientes de a uno. 
9) Al terminar el día (el cual posee un número no determinado de "turnos") el encargado recorre 
la lista recursivamente apilando todos los clientes que fueron atendidos 10 veces para enviar 
la información al gerente que les hará llegar un presente (cupón, beneficio, etc.). 
A todos los clientes que son apilados se les resetea el contador de veces atendido en el pasado.

Antes de cerrar el Banco, se envía un reporte al gerente con:
1) Cantidad de turnos del día.
2) Cantidad total de clientes del día.
*/
//librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//registros
typedef struct tipo_personas{
 char nombre[12];
 int telef;
 int dni;
 int atendido;
 int contadordeturnos;
 int contadordecliente;
}datos;

typedef struct tipo_nodo{
	datos cliente;
	struct tipo_nodo *sig;
}nodo;

typedef struct tipo_nodo_cola_pila{
	datos *cliente
	struct tipo_nodo_cola_pila *sig;
}nodo_aux;

typedef struct tipo_cola{
	nodo *primero, *ultimo;
}t_cola;


//funciones prototipo
void crear_lista(nodo **lista);
void crear_cola(t_cola *cola);
void crear_pila(nodo **pila);
void cargar_cliente(datos *cli, int dni);
nodo *insertar_cliente(nodo **lista, int dni);
void cargar_lista(nodo **lista);
nodo *buscar_cliente(nodo *lista, int dni);
void encolar_clientes(t_cola *cola, nodo *c);
int vacia(t_cola cola);
nodo *desencolar_paciente(t_cola *cola);
void apilar(nodo **pila, nodo *c);
int desapilar(nodo **pila);

int main(){
	system ("color 0C");
	nodo *lista,*cliente;
	nodo *pila;
	int dia=1;
	int dni;
	int contarclientes=0;
	int contarturnos=0;
	tcola cola;
	
	//inicializacion
	crear_lista(&lista);
	crear_pila(&pila);
	crear_cola(&cola);
	cargar_cliente(&lista);
	
	//cuerpo del programa
	//Inicializa el dia
	while(dia){
		
	//Ingresan los clientes y los encolamos:
		printf("Indique el DNI:(0 para salir) \n");
		scanf("%d", &dni);
		contarclientes=0;
	while(dni&contarclientes<=25){
	
		cliente = buscar_cliente(lista, dni);
	
		if(cliente == NULL)
			insertar_cliente(&lista, dni);
			contarclientes++;
		encolar_cliente(&cola, cliente);
		printf("Ingrese el dni: (0 para terminar) \n");
		scanf("%d", &dni);
	}
		while(!vacia(cola)){
		cliente = desencolar_clientes(&cola);
		cliente=cliente.atendido;
		
	}
	  printf ("Sigue el dia?(0 para terminar)\n");
	  scanf("%d",&dia);
	}
	recursivo(lista,&pila);
	system("pause");
	return 0;
}


//funciones 
//crear lista
void crear_lista(nodo **lista){*lista=NULL;}

//CREA LA COLA
void crear_cola(t_cola *cola){
	cola->primero=NULL;
	cola->ultimo=NULL;
}

void cargar_cliente(datos *cli, int dni){

	printf("Ingrese el nombre del paciente: \n");
	scanf("%s", cli->nombre);
	printf("Ingrese el telefono del paciente: \n");
	scanf("%d", cli->telef);
	printf("Ingrese el numero de veces que fue atendido el cliente: \n");
	scanf("%d", cli->atendido);
	cli->dni=dni;
	printf ("Registrado correctamente. \n");
	cli->contadordeturnos=1;
	cli->cliente=1;
}

//inserta un elemento en la lista


nodo *insertar_cliente(nodo **lista, int dni){
	datos cli;
	nodo *actual, *anterior;
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->clientes=cli;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->cliente.dni<cli.dni){
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

void cargar_lista(nodo **lista){
	int dni;
	printf("Ingrese el DNI (0 para terminar): \n");
	scanf("%d", &dni);
	while(dni){
		insertar_cliente(lista, dni);
		printf("Ingrese el DNI (0 para terminar): \n");
		scanf("%d", &dni);
	}
}

nodo *buscar_cliente(nodo *lista, int dni){
	nodo *aux;
	aux=lista;
	while(aux!=NULL && aux->cliente.dni != dni)
		aux=aux->sig;
	return aux;
}

void encolar_clientes(t_cola *cola, nodo *c){
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->clientes=c->clientes;
	nuevo->sig=NULL;
	if(cola->primero==NULL){
		cola->primero=nuevo;
		cola->ultimo=nuevo;
	}else{
		cola->ultimo->sig=nuevo;
		cola->ultimo=nuevo;
	}
}

int vacia(t_cola cola){
	if(cola.primero==NULL)
		return 1;
	else
		return 0;	
}

nodo *desencolar_paciente(t_cola *cola){
	nodo *aux;
	aux=cola->primero;
	cola->primero=aux->sig;
	return aux;	
}

void apilar(nodo **pila, nodo *c){
		
	nodo *nuevo;
	nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->cliente=c;
	nuevo->sig=*pila;
	*pila=nuevo;
}

int desapilar(nodo **pila){
	int valor;
	nodo *aux;
	aux=*pila;
	*pila=aux->sig;
	valor=aux->valor;
	free(aux);
	return valor;
}

int recursivo(nodo *lista,nodo_aux**pila){
	nodo *aux;
	aux=lista;
	if(aux != NULL)
	   if(aux->cliente.atendido)
		apilar(pila,aux->cliente);
		recursivo(aux->sig,pila);
			
}
