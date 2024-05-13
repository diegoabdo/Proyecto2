from tkinter import *
from estructuras.linked_list import LinkedList

from models.lista_simple_model import ListaSimpleModel
from controllers.simple_list_controller import ListaSimpleController

from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesListas


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Lista")

        # Estructura del frame
        self.lista = LinkedList()

        # Definimos el modelo de datos de la lista
        self.modelo = ListaSimpleModel(self.lista)

        # Definimos el controlador de la lista
        self.controlador = ListaSimpleController(self.modelo, self)

        # Elementos del frame
        self.titulo = Label(self, text="Lista simplemente enlazada")
        self.lista_informacion = ListaInformacion(self, self.controlador)
        self.lista_interfaz = EstructuraSimpleInterfaz(self)
        self.botones_inferiores = BotonesInferiores(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_interfaz.grid(row=1, column=0)
        self.lista_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

        # Le indicamos al controlador que nos cargue todas las listas del modelo
        self.controlador.cargar_opciones()

    # Método para actualizar toda la interfaz
    def actualizar(self, informacion):

        self.lista_informacion.actualizar(informacion)
        self.lista_interfaz.actualizar(informacion)

    def actualizar_caja_opciones(self, opciones):
        self.lista_informacion.actualizar_caja_opciones(opciones)


# Responsabilidad: Mostrar toda la información de la lista
class ListaInformacion(EstructuraInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)


# Responsabilidad: Mostrar la lista en una interfaz gráfica
class EstructuraSimpleInterfaz(EstructuraInterfaz):
    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular la lista
class BotonesInferiores(BotonesListas):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_inicio.grid(row=0, column=2)
        self.insertar_final.grid(row=0, column=3)

        self.eliminar_final.grid(row=0, column=4)
        self.eliminar_inicio.grid(row=0, column=5)

        self.buscar_button.grid(row=0, column=6)
