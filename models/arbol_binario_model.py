from .fichero import Fichero
from .templates.arbol_binario_model_template import ArbolBinarioModelTemplate


class ArbolBinarioModel(ArbolBinarioModelTemplate):
    def __init__(self, tree):
        super().__init__(tree)

        self.fichero = Fichero("recursos/datos/arboles_binarios.json")

    def insertar_raiz(self, valor):
        self.tree.insert_root(valor)

        return self.obtener_informacion()

    def insertar_izquierda(self, valor, padre):
        self.tree.insert_left(valor, padre)

        return self.obtener_informacion()

    def insertar_derecha(self, valor, padre):
        self.tree.insert_right(valor, padre)

        return self.obtener_informacion()
    
    def eliminar(self, valor):
        self.tree.delete(valor)

        return self.obtener_informacion()

    def buscar(self, valor):
        nodo_buscado = self.tree.search(valor).get_data()

        arbol_informacion = self.obtener_informacion()
        arbol_informacion.set_seleccionado(nodo_buscado)

        return arbol_informacion

    # Operaciones para guardar el árbol dentro de un fichero Json
    def guardar(self, nombre):
        # Para guardar el árbol en el Json obtenemos todos los nodos de cada nivel del arbol
        # ejemplo:
        # 0: [5] -> raíz
        # 1: [2, 3] -> hijos de raíz
        # 2: [8, 9, 4, 6] -> hijos de hijos de raíz

        self.tree.complete_tree()
        nodos_niveles = self.tree.to_list()
        niveles_dic = {}

        # Creamos un diccionario con la información de los niveles del árbol
        for i in range(len(nodos_niveles)):
            niveles_dic[i] = nodos_niveles[i]

        # Guardamos ese diccionario en el Json con la información de los niveles
        # Ejemplo:
        # {
        # "arbol1" : {
        #              0: [5],
        #              1: [2, 3],
        #              2: [8, 9, 4, 6]
        # }

        # Guardamos la información en el Json
        self.fichero.guardar_informacion(nombre, niveles_dic)

        # Obtenemos la lista de las claves del diccionario
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

    def cargar(self, nombre):

        # Para cargar un árbol obtenemos la información del Json de los niveles de este
        niveles_arbol = self.fichero.obtener_valor(nombre)

        # Ejemplo
        # "arbol1" : {
        #              0: [5],      <-- Nodo raíz
        #              1: [2, 3],   <-- Nodos del nivel 1
        #              2: [8, 9, 4, 6]  <-- Nodos del nivel 2

        # Antes de cargar la información, debemos limpiar el árbol
        self.tree.clear()

        # Lo recorremos y los insertamos en el árbol
        for nivel in niveles_arbol:
            self.tree.insert_in_level(int(nivel), niveles_arbol[nivel])

        return self.obtener_informacion()

    def remover(self, nombre):
        # Removelos la clave del Json
        self.fichero.eliminar_elemento(nombre)

        return self.cargar_opciones()
