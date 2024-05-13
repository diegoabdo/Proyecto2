class ArbolBinarioInformacion:
    def __init__(self, root, cant_nodes, profundidad, nodo_seleccionado=None, arbol_referencia=None):
        self.root = root
        self.cant_nodes = cant_nodes
        self.profundidad = profundidad
        self.nodo_seleccionado = nodo_seleccionado

        self.arbol_referencia = arbol_referencia

    def get_root(self):
        return self.root

    def get_cantidad_nodos(self):
        return self.cant_nodes

    def get_profundidad(self):
        return self.profundidad

    def set_seleccionado(self, booleano):
        self.nodo_seleccionado = booleano

    def get_seleccionado(self):
        return self.nodo_seleccionado

    def get_arbol_referencia(self):
        return self.arbol_referencia

    def set_arbol_referencia(self, arbol_referencia):
        self.arbol_referencia = arbol_referencia
