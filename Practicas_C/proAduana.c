//Enunciado:

/*En la aduana se administran los depósitos con una lista ordenada por código interno. 
Los elementos en el deposito mantienen la siguiente información: 
1) Código aduanero (numero de 10 dígitos); 
2) Antiguedad (cantidad de días que lleva el paquete en la aduana);  
3) DNI destinatario; 
4) Peso del paquete (real 5,2); y 
5) Impuesto (real 5,2). 
Al comienzo del día se reciben todos los depósitos nuevos en una cola, 
para ser agregados al listado principal. Una vez agregados los nuevos elementos, 
comienza la atención al público. Cada vez que se presenta alguien a buscar un paquete, 
se busca en la lista por número de DNI, se entrega el producto 
(removiéndolo de la lista) y se cobra el impuesto correspondiente. 
Al finalizar el día, debe informarse lo recaudado por impuestos y 
recorrer el listado recursivamente para remover y 
apilar los elementos que hace 20 días llegaron y no fueron retirados.*/


//librerias
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//registro
typedef struct tipo_aduana{
	int codigo;
	int dias;
	int dni;
	float peso;
	float impuesto;
	
}deposito;

typedef struct tipo_nodo{
	deposito aduana;
	struct tipo_nodo *sig;
}nodo;

typedef struct tipo_cola{
	nodo *primero, *ultimo;
}t_cola;

//prototipos

void crear_lista(nodo **lista);
void crear_cola(t_cola *cola);
deposito cargar_cliente(int codigo);
void encolar(t_cola *cola, deposito adu);
void insertar_ordenado(nodo **lista, deposito dato);
deposito desencolar(t_cola *cola);
int cola_vacia(t_cola cola);
void eliminar_nodo(nodo **lista, int dni);
nodo *buscar_valor(nodo *lista, int dni);
void recorrido_recursivo(nodo *lista, nodo_aux **pila);


int main(){
	system ("color 0C");
	//declaracion de variables
	nodo *lista, *elemento;
	nodo *pila;
	t_cola cola;
	float impuesto=0;
	int dni;
	int dia=1;
	int codigo;
	//inicializacion
	crear_lista(&lista);
	crear_cola(&cola);
	crear_pila(&pila);
	
	//inicia dia 
	while(dia){
		
		//Encolamos a los paquetes nuevos :
		printf("Ingrese el codigo aduanero (0 para terminar) \n");
		scanf("%d", &codigo);
		
		while(codigo){
			elemento=cargar_cliente(codigo);
			encolar(cola,elemento);
			if(elemento == NULL)
			
			     desencolar(&cola);
				insertar_ordenado(&lista, codigo);
			
			printf("Ingrese el codigo aduanero (0 para terminar) \n");
			scanf("%d", &codigo);
		}
		//atencion al publico
		printf ("Ingrese el dni (0 para terminar): \n");
		scanf("%d",&dni);
		while(dni){
			elemento=buscar_valor(lista,dni);
			if(elemento==NULL){
				printf ("No se encontro el paquete. \n");
			}
			printf ("El Impuesto por el paquete es de :$%.2f.\n",elemento->aduana.impuesto);
			impuesto=impuesto+elemento->aduana.impuesto;
			eliminar_nodo(lista,dni);
			printf ("Ingrese el dni (0 para terminar): \n");
			scanf("%d",&dni);
		}
	 printf ("Sigue dia? . \n");
	 scanf("%d",&dia);	
	}
	recorrido_recursivo(lista, &pila);
	printf ("la recaudacion de impuesto en el dia fue de : $%.2f.\n",impuesto);
	
	
	system ("pause");
	return 0;
}

/*Definición de funciones*/
//CREA LA LISTA
void crear_lista(nodo **lista){*lista=NULL;}
//CREO LA PILA
void crear_pila(nodo_aux **pila){
	*pila=NULL;
}

//CREA LA COLA
void crear_cola(t_cola *cola){
	cola->primero=NULL;
	cola->ultimo=NULL;
}

//carga los datos del paquete
deposito cargar_cliente(int codigo){
	deposito aduana;
	aduana.codigo=codigo;
	printf("Ingrese el numero de dni : \n");
	scanf("%d", &aduana.dni);
	printf("Ingrese la cantidad de dias que ha estado el paquete:  \n");
	scanf("%d", &aduana.dias);
	printf ("Ingrese el peso del paquete: \n");
	scanf("%f",&aduana.peso);
	printf("Ingrese el impuesto a cobrar por la entrega del paquete: \n");
	scanf("%f",&aduana.impuesto);
	
	return aduana;
}

//ENCOLAR UN ELEMENTO
void encolar(t_cola *cola, deposito adu){
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->adu=adu;
	nuevo->sig=NULL;
	if(cola->primero==NULL){
		cola->primero=nuevo;
		cola->ultimo=nuevo;
	}else{
		cola->ultimo->sig=nuevo;
		cola->ultimo=nuevo;
	}
}
//INSERTA UN NODO ORDENADO A LA LISTA
void insertar_ordenado(nodo **lista, deposito dato){
	nodo *actual, *anterior;
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->aduana=dato;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->aduana.codigo<deposito.codigo){
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
/*Antes de invocar a descencolar debe 
verificarse que la cola no este vacia*/
deposito desencolar(t_cola *cola){
	nodo *aduana;
	nodo *aux;
	aux=cola->primero;
	cola->primero=aux->sig;
	aduana=aux->aduana;
	free(aux);
	return aduana;
}

//VERIFICA SI LA COLA ESTA VACIA
int cola_vacia(t_cola cola){
	if(cola.primero==NULL)
		return 1;
	else
		return 0;
}
//busca el paquete dentro de la lista
nodo *buscar_valor(nodo *lista, int dni){
	nodo *aux;
	aux=lista;
	while(aux!=NULL && aux->aduana.dni!=dni)
		aux=aux->sig;
	return aux->aduana;
}

//elimina un nodo esto se va a usar en la parte final,cuando se entregue el paquete
void eliminar_nodo(nodo **lista, int dni){
	nodo *actual, *anterior;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->aduana.dni!=dni){
		anterior=actual;
		actual=actual->sig;
	}
	if(actual!=NULL){	/*dato encontrado*/
		if(anterior!=NULL){	/*borrar del cuerpo*/
			anterior->sig=actual->sig;
		}else{				/*borrar del inicio*/
			*lista=actual->sig;
		}
		free(actual);
	}
}
void apilar_paquete(nodo_aux **pila, deposito aduana){
	nodo_aux *nuevo;
	nuevo=(nodo_aux *)malloc(sizeof(nodo_aux));
	nuevo->aduana=aduana;
	nuevo->sig=*pila;
	*pila=nuevo;	
}


//tiene que recorrer la lista, y encontrar paquetes con 20 dias y entonces los elimina de la lista y los apila
void recorrido_recursivo(nodo *lista, nodo **pila){
	int dni;
	nodo *aux;
	aux=lista;
	if(aux!=NULL){
		if(aux->aduana.dias == 20)
			apilar_paquete(pila, aux->aduana);
			eliminar_nodo(lista, aux->aduana.dni);
		recorrido_recursivo(&aux->sig, pila);
	}	
}
