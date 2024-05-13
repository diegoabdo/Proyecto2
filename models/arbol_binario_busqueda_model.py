from .fichero import Fichero
from .templates.arbol_binario_model_template import ArbolBinarioModelTemplate


class ArbolBinarioBusquedaModel(ArbolBinarioModelTemplate):
    def __init__(self, tree):
        super().__init__(tree)

        self.fichero = Fichero("recursos/datos/arboles_busqueda.json")

    def insertar_raiz(self, valor):

        # Comprobamos si se trata de un entero
        if isinstance(valor, int):
            self.tree.insert_root(valor)

            return self.obtener_informacion()

        # Comprobamos si se trata de un valor numérico
        elif valor.isdigit():
            self.tree.insert_root(int(valor))

            return self.obtener_informacion()

        self.tree.insert_root(valor)
        return self.obtener_informacion()

    def insertar(self, valor):
        # Comprobamos si el valor es un entero
        if isinstance(valor, int):
            self.tree.insert(valor)

            return self.obtener_informacion()

        # Comprobamos si el valor de la cadena es un digito
        elif valor.isdigit():
            self.tree.insert(int(valor))

            return self.obtener_informacion()

        # Comprobamos si es un valor flotante
        try:
            valor = float(valor)
            self.tree.insert(valor)

            return self.obtener_informacion()

        except ValueError:
            pass

        # De llegar aquí, damos por hecho que el valor es una cadena
        self.tree.insert(valor)
        return self.obtener_informacion()

    def eliminar(self, valor):
        # Comprobamos si el valor es un entero
        if valor.isdigit():
            self.tree.delete(int(valor))

            return self.obtener_informacion()

        # Comprobamos si el valor es un valor flotante
        try:
            self.tree.delete(float(valor))

            return self.obtener_informacion()

        except ValueError:
            pass

        # De llegar aquí, damos por hecho que el valor es una cadena
        self.tree.delete(valor)

        return self.obtener_informacion()

    def buscar(self, valor):

        arbol_informacion = self.obtener_informacion()

        # Comprobamos si el valor es un entero
        if valor.isdigit():
            nodo_buscado = self.tree.search(int(valor)).get_data()
            arbol_informacion.set_seleccionado(nodo_buscado)

            return arbol_informacion

        # Comprobamos si el valor es un valor flotante
        try:
            nodo_buscado = self.tree.search(float(valor)).get_data()
            arbol_informacion.set_seleccionado(nodo_buscado)

            return arbol_informacion

        except ValueError:
            pass

        # De llegar aquí, damos por hecho que el valor es una cadena no numérica
        nodo_buscado = self.tree.search(valor).get_data()
        arbol_informacion.set_seleccionado(nodo_buscado)

        return arbol_informacion

        # De no ser un entero, damos por hecho de que es una cadena con valores

    # -------- OPERACIONES QUE INTERACTUAN CON EL FICHERO DEL ÁRBOL --------
    def guardar(self, nombre):
        # Obtenemos una lista de los árboles en orden de niveñ
        nodos_niveles = self.tree.to_list()

        # Guardamos la información en el Json
        self.fichero.guardar_informacion(nombre, nodos_niveles)

        # Obtenemos los elementos de árboles de búsqueda del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles

    def cargar(self, nombre):
        # Obtenemos la lista de nodos del árbol dentro del Json
        nodos_arbol = self.fichero.obtener_valor(nombre)

        # Limpiamos el árbol actual
        self.tree.clear()

        # Los insertamos en el árbol
        for nodo in nodos_arbol:
            self.tree.insert(nodo)

        return self.obtener_informacion()

    def remover(self, nombre):
        # Removemos el árbol del Json
        self.fichero.eliminar_elemento(nombre)

        # Devolvemos la información de las estructuras del json
        return self.cargar_opciones()
