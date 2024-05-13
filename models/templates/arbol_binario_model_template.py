from models.entities.arbol_binario import ArbolBinarioInformacion


class ArbolBinarioModelTemplate:
    def __init__(self, tree):
        self.tree = tree
        self.fichero = None

    def obtener_informacion(self):
        # Datos necesarios para el árbol
        # 1. Raíz
        # 2. Nodos: [NodoInformacion]
        # 3. Profundidad

        # Datos necesarios para cada nodo (NodoInformacion)
        # 1. Dato
        # 2. Id
        # 3. Tiene hijo derecho: bool
        # 4. Tiene hijo izquierdo: bool

        # Estos datos que devolvemos serán los necesarios para que la vista pueda dibujar correctamente el árbol
        # Y además para mostrar la información del árbol

        root = self.tree.get_root()  # Raiz del árbol
        cantidad_nodos = self.tree.count_nodes()  # Cantidad de nodos del árbol
        profundidad = self.tree.max_depth()  # Profundidad del árbol

        arbol_informacion = ArbolBinarioInformacion(root, cantidad_nodos, profundidad)

        # Le enviamos al árbol información la referencia del árbol
        arbol_informacion.set_arbol_referencia(self.tree)

        return arbol_informacion

    # ---- FUNCIONES PARA INTERACTUAR CON EL FICHERO DE INFORMACIÓN ------
    def cargar_opciones(self):
        # Obtenemos todos los elementos de árbol del Json
        elementos_arbol = self.fichero.obtener_elementos()
        nombres_arboles = [nombre for nombre in elementos_arbol]

        return nombres_arboles
