from tkinter import *
from estructuras.circular_list import CircularList

from models.lista_circular_model import ListaCircularModel
from controllers.lista_circular_controller import ListaCircualarController

from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesListas


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaCircularView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Circular")

        # Estrucuta
        self.lista = CircularList()

        # Definimos el modelo de datos
        self.modelo = ListaCircularModel(self.lista)

        # Definimos el controlador de la lista
        self.controlador = ListaCircualarController(self.modelo, self)

        # Elementos del frame
        self.titulo = Label(self, text="Lista Circular")
        self.informacion_lista = ListaCircularInformacion(self, self.controlador)
        self.lista_interfaz = EstructuraCircularInterfaz(self)
        self.botones_inferiores = BotonesCircular(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.informacion_lista.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

        self.controlador.cargar_opciones()

    # Método para actualizar toda la interfaz
    def actualizar(self, lista_circular_informacion):
        self.lista_interfaz.actualizar(lista_circular_informacion)
        self.informacion_lista.actualizar(lista_circular_informacion)

    def actualizar_caja_opciones(self, opciones):
        self.informacion_lista.actualizar_caja_opciones(opciones)


# Responsabilidad: Mostrar la información de la lista circular
class ListaCircularInformacion(EstructuraInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)


# Responsabilidad: Mostrar la lista circular en una interfaz gráfica
class EstructuraCircularInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones inferiores para manipular la lista circular
class BotonesCircular(BotonesListas):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Elementos del frame
        self.rotar_izquierda_button = Button(self, text="Rotar Izquierda", command=self.rotar_izquierda)
        self.rotar_derecha_button = Button(self, text="Rotar Derecha", command=self.rotar_derecha)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.rotar_izquierda_button.grid(row=0, column=2)
        self.rotar_derecha_button.grid(row=0, column=3)

        self.insertar_inicio.grid(row=0, column=4)
        self.insertar_final.grid(row=0, column=5)

        self.eliminar_inicio.grid(row=0, column=6)
        self.eliminar_final.grid(row=0, column=7)

        self.buscar_button.grid(row=0, column=8)

    # Métodos de la lista
    def rotar_izquierda(self):
        self.controlador.rotar_izquierda()

    def rotar_derecha(self):
        self.controlador.rotar_derecha()
