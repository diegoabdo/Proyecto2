from .fichero import Fichero

from .entities.estructura_lineal import *


# Modelo para the pila
class PilaModel:
    def __init__(self, stack):
        self.stack = stack
        self.fichero = Fichero('recursos/datos/pilas.json')

    def push(self, elemento):
        self.stack.push(elemento)

        return self.obtener_informacion()

    def pop(self):
        self.stack.pop()

        return self.obtener_informacion()

    def search(self, elemento):

        informacion = self.obtener_informacion()
        nodo_buscado = self.stack.search(elemento)

        informacion.set_selected_node(nodo_buscado)

        return informacion

    def guardar(self, nombre):
        # Obtenemos la lista en forma de una lista para guardarlo en el Json
        lista_pila = self.stack.to_list()

        # Guardamos la información proporcionada en el Json con el siguiente formato
        # {
        # 'pila1': [1, 2, 3, 4, 5, 6, 7]
        # }
        self.fichero.guardar_informacion(nombre, lista_pila)

        # Procesamos cuantós elementos de pilas existen en el fichero
        elementos_pilas = self.fichero.obtener_elementos()

        # Obtenemos solamente las claves de los diccionarios
        # Obtenemos todos los elementos cola del fichero json
        # {
        # clave :    valor
        # 'pila1: [1, 2, 3],
        # 'pila2: [5, 3, 9]
        # }
        lista_nombres = [elemento for elemento in elementos_pilas]

        return lista_nombres

    def cargar(self, nombre):
        # Obtenemos la lista que almacena el nombre de la pila que seleccionamos
        pila_elementos = self.fichero.obtener_valor(nombre)

        # Limpiamos la pila actual
        self.stack.clear()

        # Procesamos la lista para guardarla en la pila del modelo
        # Invertimos la lista
        pila_elementos.reverse()

        for elemento in pila_elementos:
            self.stack.push(elemento)

        return self.obtener_informacion()

    def eliminar(self, nombre):
        # Eliminamos el elemento
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()

    def cargar_opciones(self):
        # Obtenemos todos los elementos de las pilas
        pilas_datos = self.fichero.obtener_elementos()

        # Obtenemos solamente los nombres
        lista_nombres = [elemento for elemento in pilas_datos]

        return lista_nombres

    def obtener_informacion(self):

        # Obtenemos la siguiente información para la pila
        # Tope
        # Fondo
        # Tamaño
        # Tamaño máximo
        # Nodos

        estructura_informacion = EstructuraLinealInformacion(
            self.stack.get_head(),
            self.stack.get_tail(),
            self.stack.get_size(),
            self.stack.get_max(),
        )

        # Ahora procesamos los nodos de la lista
        lista_nodos = self.stack.to_list(references=True)

        # Por cada nodo creamos un objeto de tipo NodoInformacion
        for nodo in lista_nodos:
            estructura_informacion.list_nodes.append(
                NodoInformacion(nodo.get_data(), id(nodo))
            )

        return estructura_informacion
