/*Una ferretería maneja su catálogo de productos con una lista ordenada por código de producto que 
tiene la siguiente información: 
1) Código de producto. 
2) Categoría. 
3) Tipo de producto. 
) Tamaño.
5) Stock actual. 
6) Stock mínimo. 
7) Stock máximo. 
8) Precio.
 Al comenzar el día se atiende al proveedor que presenta 3 pilas de productos: 
1) La pila de productos nuevos (que no están en la lista). 
2) La pila de productos de reposición (para actualizar el stock de la lista, o el precio).
3) La pila de productos a retirar del mercado (para eliminar de la lista). 
Cuando se atiende un cliente, éste va realizando distintos pedidos y el empleado ingresa los datos 
que requiere para la búsqueda (categoría, tipo, tamaño y cantidad). Si la cantidad de un producto 
que pide el cliente es menor al stock actual, la venta se realiza sin problemas, de lo contrario, 
la venta se efectúa hasta la cantidad que hay en existencia de ese producto. 
Cuando se finaliza la atención del cliente, debe actualizarse el stock e informar el precio de 
lo pedido. Al finalizar el día, se recorre la lista recursivamente para armar una cola de pedidos 
con aquellos productos cuyo stock está por debajo de la cantidad mínima.

Desarrolle un algoritmo que realice el registro diario de la operatoria descripta emulando 
el proceso completo y obtenga cada uno de los puntos requeridos.
*/

//librerias 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//registro
typedef struct tipo_producto{
	int codigodeproducto;
	char categoria[20];
	char tipodeproducto[20];
    float tamano;
    int stockactual,stockminimo,stockmaximo;
    float precio;
	
}producto;

typedef struct tipo_nodo{
	producto prod;
	struct tipo_nodo *sig;
}nodo;

/*Funciones prototipo*/
void crear_lista(nodo **lista);
void insertar_ordenado(nodo **lista, producto dato);
void eliminar_nodo(nodo **lista, int codigoproducto);
void apilar(nodo **pila, producto dato);
int desapilar(nodo **pila);
int pila_vacia(nodo *pila);


int main(){
	system ("color 0C");
	//crear variables
	nodo *lista, *producto;
	int sigue_dia=1;
	nodo *pila;
	
	
	//inicializar
	crear_lista(&lista);
	crear_pila(&pila);
	crear_pila(&pila_nuevos)
	crear_pila(&pila_)
	cargar_pila(&pila);
	
	while(sigue_dia){
		//funcion tipo proveedor 
		while(eleccion!=0){
			eleccion=menu();
			switch(eleccion){
				case 1 : pila_nuevos();{
					break;
				}
				case 2 : pila_reposicion();{
					break;
				}
				case 3 : pila_retirardelmercado(){
					
					break;
				}
			}
          producto=desapilar(&pila);
          insertar_paquete(&lista, producto);
        }
    
    
	}
	
	
	
	system("pause");
	return 0;
}

//funciones
//crea lista
void crear(nodo **t_nodo){
     *t_nodo=NULL;
}

producto cargar_producto(){
        producto prod;
        printf("Ingrese el codigo de producto: \n");
        scanf("%d", &prod.codigodeproducto);
        printf("Ingrese el tipo de producto: \n");
        scanf("%s", &prod.tipodeproducto);
        printf("Ingrese la categoria del producto: \n");
        scanf("%s", &prod.categoria);
        printf("Ingrese el stock minimo del producto: \n");
        scanf("%d", &prod.stockminimo);
        printf("Ingrese el stock maximo del producto: \n");
        scanf("%d", &prod.stockmaximo);
        printf("Ingrese el stock actual del producto: \n");
        scanf("%d", &prod.stockactual);
        printf("Ingrese el precio: \n");
        scanf("%f", &prod.precio);
        printf("Ingrese el tamano : \n");
        scanf("%f", &prod.tamano);
        return prod;
}

void insertar_ordenado(nodo **lista, producto dato){
	nodo *actual, *anterior;
	nodo *nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->prod=dato;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->prod.codigodeproducto<dato.codigodeproducto){
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

void eliminar_nodo(nodo **lista, int codigoproducto){
	nodo *actual, *anterior;
	actual=*lista;
	anterior=NULL;
	while(actual!=NULL && actual->prod.codigodeproducto!=codigoproducto){
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

//APILA UN ELEMENTO EN LA PILA
void apilar(nodo **pila, producto dato){
	nodo *nuevo;
	nuevo=(nodo *)malloc(sizeof(nodo));
	nuevo->prod=dato;
	nuevo->sig=*pila;
	*pila=nuevo;
}

//DESAPILA UN ELEMENTO DE LA PILA
 desapilar(nodo **pila){
	int valor;
	nodo *aux;
	aux=*pila;
	*pila=aux->sig;
	valor=aux->valor;
	free(aux);
	return valor;
}
//INDICA SI LA PILA ESTA VACÍA
int pila_vacia(nodo *pila){
	if(pila==NULL)
		return 1;
	else
		return 0;
}

void cargar_pila(nodo **pila){
     int hay_productos=1;
     producto prod;
     while(hay_productos){
           prod=cargar_producto();
           apilar(pila, prod);
           printf("Hay mas producto que quiera ingresar? (0 para terminar) \n");
           scanf("%d", &hay_paquetes);
	}
}

int menu(){
	int eleccion;
	system("CLS");
	printf("\n********** MENU - PROVEEDOR - **********\n");
	printf("1. PRODUCTOS NUEVOS \n");
	printf("2. PRODUCTOS DE REPOSICION \n");	
	printf("3. PRODUCTO A RETIRAR DEL MERCADO \n");
	printf("0. SALIR\n");
	printf("\n\nElegir: ");
	scanf("%d", &eleccion);
	return eleccion;
}

