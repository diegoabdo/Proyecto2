from tkinter import *
from estructuras.double_linked_list import DoubleLinkedList

from models.lista_doble_model import ListaDoblementeEnlazadaModel
from controllers.lista_doble_controller import ListaDobEnlazadaController

from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesListas


# Responsabilidad: Mostrar todos los elementos de la interfaz
class ListaDobEnView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Lista Doble Enlazada")

        # Estructura
        self.lista = DoubleLinkedList()

        # Definimos el modelo de datos
        self.modelo = ListaDoblementeEnlazadaModel(self.lista)

        # Definimos el controlador de la lista
        self.controlador = ListaDobEnlazadaController(self.modelo, self)

        # Elementos del frame
        self.titulo = Label(self, text="Lista Doble Enlazada")
        self.lista_dob_informacion = ListaDobInformacion(self, self.controlador)
        self.lista_dob_interfaz = ListaDobEnlazadaInterfaz(self)
        self.botones_inferiores = BotonesDobEnlazada(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.lista_dob_interfaz.grid(row=1, column=0)
        self.lista_dob_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

        self.controlador.cargar_opciones()

    # Método para actualizar toda la interfaz
    def actualizar(self, lista_informacion):
        self.lista_dob_informacion.actualizar(lista_informacion)
        self.lista_dob_interfaz.actualizar(lista_informacion)

    def actualizar_caja_opciones(self, opciones):
        self.lista_dob_informacion.actualizar_caja_opciones(opciones)


# Responsabilidad: Mostrar toda la información de la lista
class ListaDobInformacion(EstructuraInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)


# Responsabilidad: Mostrar la lista enlazada en una interfaz gráfica
class ListaDobEnlazadaInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones de la lista para manipularla
class BotonesDobEnlazada(BotonesListas):

    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Elementos del frame
        self.indice_label = Label(self, text="Indice: ")
        self.indice_entry = Entry(self)

        self.insertar_posicion_button = Button(self, text="Insertar en posicion", command=self.insertar_posicion)
        self.eliminar_posicion_button = Button(self, text="Eliminar en posicion", command=self.eliminar_posicion)

        # Posicionamiento de los elementos
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.indice_label.grid(row=0, column=2)
        self.indice_entry.grid(row=0, column=3)

        self.insertar_posicion_button.grid(row=0, column=4)
        self.eliminar_posicion_button.grid(row=0, column=5)

        self.insertar_final.grid(row=0, column=6)
        self.insertar_inicio.grid(row=0, column=7)

        self.eliminar_final.grid(row=0, column=8)
        self.eliminar_inicio.grid(row=0, column=9)

        self.buscar_button.grid(row=0, column=10)

    # Métodos de la lista
    def insertar_posicion(self):
        dato = self.dato_entry.get()
        indice = int(self.indice_entry.get())

        self.controlador.insertar_por_indice(dato, indice)

    def eliminar_posicion(self):
        indice = int(self.indice_entry.get())

        self.controlador.eliminar_por_indice(indice)
