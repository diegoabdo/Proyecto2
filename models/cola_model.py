from .fichero import Fichero
from .entities.estructura_lineal import *


# Modelo para el queue
class ColaModel:
    def __init__(self, queue):
        self.queue = queue
        self.fichero = Fichero('recursos/datos/colas.json')

    def enqueue(self, nombre):
        self.queue.enqueue(nombre)

        return self.obtener_informacion()

    def dequeue(self):
        self.queue.dequeue()

        return self.obtener_informacion()

    def search(self, nombre):
        informacion = self.obtener_informacion()
        nodo_buscado = self.queue.search(nombre)

        informacion.set_selected_node(nodo_buscado)

        return informacion

    def guardar(self, nombre):
        # Obtenemos todos los elementos de la cola en una lista
        lista_elementos = self.queue.to_list()
        # Guardamos la información proporcionada en el Json con el siguiente formato
        # {
        # 'cola1': [1, 2, 3, 4, 5, 6, 7]
        # }
        self.fichero.guardar_informacion(nombre, lista_elementos)

        # Obtenemos todos los elementos cola del fichero json
        # {
        # clave :    valor
        # 'cola1: [1, 2, 3],
        # 'cola2: [5, 3, 9]
        # }
        elementos_cola = self.fichero.obtener_elementos()

        # Listamos solamente las claves de las colas
        lista_nombres = [elemento for elemento in elementos_cola]

        return lista_nombres

    def cargar(self, nombre):
        # Obtenemos la lista que almacena la clave que deseamos
        cola_elementos = self.fichero.obtener_valor(nombre)

        # Vacíamos la cola existente
        self.queue.clear()

        # Añadimos los elementos
        for elemento in cola_elementos:
            self.queue.enqueue(elemento)

        return self.obtener_informacion()

    def eliminar(self, nombre):
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()

    def cargar_opciones(self):
        # Obtenemos todos los elementos de las colas
        elementos_cola = self.fichero.obtener_elementos()

        # {
        #  clave:    valor
        # 'cola1: [1, 2, 3],
        # 'cola2: [5, 3, 9]
        # }

        # Obtenenmos solo las claves de los diccionarios
        lista_nombres = [elemento for elemento in elementos_cola]

        return lista_nombres

    def obtener_informacion(self):

        # Obtenemos la siguiente información para la pila
        # Tope
        # Fondo
        # Tamaño
        # Tamaño máximo
        # Nodos

        estructura_informacion = EstructuraLinealInformacion(
            self.queue.get_head(),
            self.queue.get_tail(),
            self.queue.get_size(),
            self.queue.get_max()
        )

        # Ahora procesamos los nodos de la lista
        lista_nodos = self.queue.to_list(references=True)

        # Por cada nodo creamos un objeto de tipo NodoInformacion
        # Comprobamos que la lista contenga elementos

        for nodo in lista_nodos:
            estructura_informacion.list_nodes.append(
                NodoInformacion(nodo.get_data(), id(nodo))
            )

        return estructura_informacion
