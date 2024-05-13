from models.entities.estructura_lineal import *


# Models for the lists
# Responsabilidad: Interactuar directamente con la estructura y con el fichero de configuración
class ListaModelTemplate:
    def __init__(self, list_name):
        self.list = list_name
        self.fichero = None

    def insertar_inicio(self, elemento):
        self.list.prepend(elemento)

        return self.obtener_informacion()

    def insertar_final(self, elemento):
        self.list.append(elemento)

        return self.obtener_informacion()

    def eliminar_inicio(self):
        self.list.remove_head()

        return self.obtener_informacion()

    def eliminar_final(self):
        self.list.remove_tail()

        return self.obtener_informacion()

    def buscar(self, elemento):
        nodo_buscado = self.list.search(elemento)

        informacion = self.obtener_informacion()
        informacion.set_selected_node(nodo_buscado)

        return informacion

    def guardar(self, nombre):
        # Obtenemos todos los elementos de la lista actual
        lista_elementos = self.list.to_list()

        # Guardamos en el Json la clave con su valor
        # Ejemolo: lista_elementos = {'nombre': 'lista_elementos'}
        self.fichero.guardar_informacion(nombre, lista_elementos)

        # Obtenemos todos los elementos lista del fichero
        lista_elementos_fichero = self.fichero.obtener_elementos()

        # Obtenemos solamente las claves (Nombres de las listas) de los elementos
        lista_nombres_elementos = [nombre for nombre in lista_elementos_fichero]

        return lista_nombres_elementos

    def cargar(self, nombre):

        # Obtenemos la lista de elementos del fichero del nombre pasado por parámetro
        lista_elementos = self.fichero.obtener_valor(nombre)

        # Vaciamos la list actual
        self.list.clear()

        # Insertamos los elementos de la lista en la lista actual
        for elemento in lista_elementos:
            self.list.append(elemento)

        return self.obtener_informacion()

    def eliminar(self, nombre):
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()

    def cargar_opciones(self):
        # Obtenemos todos los elementos lista del fichero
        lista_elementos_fichero = self.fichero.obtener_elementos()

        # Obtenemos solamente las claves (Nombres de las listas) de los elementos
        lista_nombres = [nombre for nombre in lista_elementos_fichero]

        return lista_nombres

    def obtener_informacion(self):

        # Obtenemos las siguiente información para la información de la lista
        # 1. head
        # 2. tail
        # 3. size
        # 5. Lista de nodos

        estructura_informacion = EstructuraLinealInformacion(
            self.list.get_head(),
            self.list.get_tail(),
            self.list.get_size()
        )

        # Ahora procesamos los nodos de la lista
        lista_nodos = self.list.to_list(references=True)

        # Por cada nodo creamos un objeto de tipo NodoInformacion
        for nodo in lista_nodos:
            estructura_informacion.list_nodes.append(
                NodoInformacion(nodo.get_data(), id(nodo))
            )

        return estructura_informacion
