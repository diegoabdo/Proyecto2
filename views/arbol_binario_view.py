from tkinter import *
from estructuras.binary_tree import BinaryTree

from models.arbol_binario_model import ArbolBinarioModel
from controllers.arbol_binario_controller import ArbolBinarioController

from .templates.inf_arbol_template import ArbolInformacion
from .templates.arbol_template import ArbolInterfaz
from .templates.botones_arbol_template import BotonesArbol


# Responsabilidad: Posicionar todos los elementos visibles en la ventana
class ArbolBinarioView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Arbol binario")

        # Estructura de dato que usaremos
        self.arbol = BinaryTree()

        # Definimos el modelo de los datos
        self.modelo = ArbolBinarioModel(self.arbol)

        # Definimos el controlador de los datos
        self.controlador = ArbolBinarioController(self.modelo, self)

        self.titulo = Label(self, text="Arbol Binario simple")
        self.arbol_informacion = ArbolBinarioInformacion(self, self.controlador)
        self.arbol_interfaz = ArbolBinarioInterfaz(self)
        self.botones_arbol = BotonesArbolBinario(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.arbol_interfaz.grid(row=1, column=0)
        self.arbol_informacion.grid(row=1, column=1)
        self.botones_arbol.grid(row=2, column=0)

        self.controlador.cargar_opciones()

    def mostrar_arbol(self, arbol_informacion):
        self.arbol_interfaz.actualizar(arbol_informacion)
        self.arbol_informacion.actualizar(arbol_informacion)

    def actualizar_caja_opciones(self, opciones):
        self.arbol_informacion.actualizar_caja_opciones(opciones)


# Responsabilidad: Mostrar toda la información del árbol (tamaño, altura, profundidad)
class ArbolBinarioInformacion(ArbolInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)


# Responsabilidad: Mostrar el árbol en una interfaz gráfica
class ArbolBinarioInterfaz(ArbolInterfaz):
    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular la información del árbol
class BotonesArbolBinario(BotonesArbol):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.insertar_derecha = Button(self, text="Insertar Derecha", command=self.insertar_derecha)
        self.insertar_izquierda = Button(self, text="Insertar Izquierda", command=self.insertar_izquierda)

        self.referencia_label = Label(self, text="Referencia: ")
        self.referencia_entry = Entry(self)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.referencia_label.grid(row=0, column=2)
        self.referencia_entry.grid(row=0, column=3)

        self.insertar_raiz.grid(row=0, column=4)

        self.insertar_derecha.grid(row=0, column=5)
        self.insertar_izquierda.grid(row=0, column=6)

        self.eliminar.grid(row=0, column=7)
        self.buscar.grid(row=0, column=8)

    def insertar_izquierda(self):
        dato = self.dato_entry.get()
        referencia = self.referencia_entry.get()

        self.controlador.insertar_izquierda(dato, referencia)

    def insertar_derecha(self):
        dato = self.dato_entry.get()
        referencia = self.referencia_entry.get()

        self.controlador.insertar_derecha(dato, referencia)
