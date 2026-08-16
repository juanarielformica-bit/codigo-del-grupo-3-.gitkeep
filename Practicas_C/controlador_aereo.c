// controlador aereo  

//Librerías:
#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

//registros 

//Estructuras de datos:
typedef struct tipo_avion{
	int capacidad;
	char aerolinea [20];
	int identificador;
	int tiemporetraso;
	int pasajeros;
	int numerodevuelo;
}avion;

typedef struct tipo_nodo{
	avion avi;
	struct tipo_nodo *sig;
}nodo;

typedef struct tipo_cola{
	nodo *primero, *ultimo;
}t_cola;

/*Funciones prototipo*/
void crear_lista(nodo **lista);
void crear_cola(t_cola *cola);
void cargar_avion(nodo *avion);
nodo *insertar_ordenado(nodo **lista, int identificador );
nodo *buscar_avion(nodo *lista, int identificador);
void encolar_avion(t_cola *cola, nodo *a);
int cola_vacia(t_cola cola);
nodo *desencolar_avion(t_cola *cola);
void cargar_tiempo_de_retraso(nodo *avion);
int sumar_tiempo_de_retraso(nodo *lista);


int main (){
	system ("Color 0C");
	//variables
	nodo *lista,*lista2 ,*avion1;
	t_cola cola;
	avion a;
	int identificador, ciclo=1;
	int aterrizajeretrasado=0;
	int aviones=1;
	
	//Inicializaciones
	crear_lista(&lista);
	crear_lista(&lista2);
	crear_cola(&cola);
	cargar_avion(&lista);
	
	//inciailiza el trabajo
	while(ciclo){
		
		//Ingresan los aviones y los enlisto:
	  while(aviones){
		printf("Indique el identificador del avion: \n");
		scanf("%d", &identificador);
		avion1 = buscar_avion(lista, identificador);
		if(avion1->avi.identificador == identificador );
		printf ("Ingrese el numero actual de nuevo de vuelo: \n");
		scanf("%d",avion1->avi.numerodevuelo);
				avion.numerodevuelo = avion1->avi.numerodevuelo;
		printf ("Ingrese la cantidad de pasajeros nuevamente: \n");
		scanf("%d",avion1->avi.pasajeros);
			avion.pasajeros=avion1->avi.pasajeros;
		if(avion1 == NULL)
		avion1=cargar_avion();
		avion1 = insertar_ordenado(lista,identificador );
		
		
		//autorizacion recibida se encola en una lista para el aterrizaje
		encolar_avion(&cola,avion);
	  } 
	  printf ("fin de ciclo");	
	}
	 //vacio la lista, agrego
	 while(!vacia(cola)){
		avion1 = desencolar_avion(&cola);
		insertar_ordenado(lista2,avion1.avi.identificador ):
		cargar_tiempo_de_retraso();
	}
	
	aterrizajeretrasado=sumar_tiempo_de_retraso(&lista);
	
	//Muestro resultados:
	printf("La cantidad de vuelos retrasados en este ciclo : %d \n",aterrizajeretrasado );
	
	
	system("Pause");
	return 0;
}

/*Definición de funciones*/
void crear_lista(nodo **lista){*lista=NULL;}

//CREA LA COLA
void crear_cola(t_cola *cola){
	cola->primero=NULL;
	cola->ultimo=NULL;
}
//Cargar avion
void cargar_avion(nodo *avion){
	printf("Ingrese la aerolinea: \n");
	scanf("%c", &avion->aerolinea.codigo);
	printf("Ingrese la capacidad del avion: \n");
	scanf("%d", &avion->capacidad.precio);
	printf("Ingrese el identificador: \n");
	scanf("%d", &avion->identificador.stock_actual);
	printf ("Ingrese la cantidad de pasajeros : \n");
	scanf("%d",&avion->pasajeros);
	printf("Ingrese el numero de vuelo: \n");
	scanf("%d",&avion->numerodevuelo);
    avion->tiemporetraso=0;
}
//INSERTA UN NODO A LA LISTA
nodo *insertar_ordenado(nodo **lista, int identificador ){
	nodo *actual, *anterior;
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->avi=avion;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->avi.identificador<avion.identificador){
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
}
nodo *buscar_avion(nodo *lista, int identificador){
	nodo *aux;
	aux=lista;
	while(aux!=NULL && aux->avi.identificador != identificador);
		aux=aux->sig;
	return aux;
}
//encola a los aviones autorizados
void encolar_avion(t_cola *cola, nodo *a){
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->avi=a->avi;
	nuevo->sig=NULL;
	if(cola->primero==NULL){
		cola->primero=nuevo;
		cola->ultimo=nuevo;
	}else{
		cola->ultimo->sig=nuevo;
		cola->ultimo=nuevo;
	}
}
//VERIFICA SI LA COLA ESTA VACIA
int cola_vacia(t_cola cola){
	if(cola.primero==NULL)
		return 1;
	else
		return 0;
}
//desencola un avion al aterrizar 
nodo *desencolar_avion(t_cola *cola){
	nodo *aux;
	aux=cola->primero;
	cola->primero=aux->sig;
	free(aux);
	return aux;	
}
//pide que ingreses el tiempo que se retrasaron los vuelos
void cargar_tiempo_de_retraso(nodo *avion){
	
	printf("Ingrese el tiempo de retraso: \n");
	scanf("%d",&avion->tiemporetraso);
}
//hace un recorrido recursivo sumando cada vuelo retrasado
int sumar_tiempo_de_retraso(nodo *lista){
	nodo *aux;
	aux=lista;
	if(aux == NULL)
		return 0;
	else
		return (aux->avi + sumar_tiempo_de_retraso(aux->sig));	
}
