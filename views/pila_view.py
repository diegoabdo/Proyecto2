from tkinter import *
from estructuras.pila import Pila

from controllers.pila_controller import PilaController
from models.pila_model import PilaModel

from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesBasicos


# Responsabilidad: Mostrar todos los elementos visibles
class PilaView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de datos Pila")

        # Atributos
        # Estructura de la clase
        self.pila = Pila()

        # Definimos el modelo y el controlador de la clase
        self.modelo = PilaModel(self.pila)
        self.controlador = PilaController(self.modelo, self)

        # Elementos del frame
        self.label_titulo = Label(self, text="Pila")
        self.pila_informacion = PilaInformacion(self, self.controlador)
        self.pila_interfaz = PilaInterfaz(self)
        self.botones_inferiores = BotonesPila(self, self.controlador)

        # Posicionamiento de los elementos
        self.label_titulo.grid(row=0, column=0)
        self.pila_interfaz.grid(row=1, column=0)
        self.pila_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

        self.controlador.cargar_opciones()

    # Método de la view para dibujar la estrucutura en pantall y actualizar los datos
    def actualizar(self, informacion_pila):

        self.pila_informacion.actualizar(informacion_pila)
        self.pila_interfaz.actualizar(informacion_pila, 'Vertical')

    # Actualizamos la caja de opciones que el usuario tiene para guardar y elegir elementos
    def actualizar_pila_opciones(self, lista_opciones):
        self.pila_informacion.actualizar_caja_opciones(lista_opciones)


# Responsabilidad: Mostrar toda la información de la pila
class PilaInformacion(EstructuraInformacion):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.maximo_variable = StringVar(self)

        # Elementos del frame
        self.maximo = Label(self, textvariable=self.maximo_variable, bg="#1A3C40", fg="white")

        # Posicionamiento de los elementos
        self.maximo.grid(row=1, column=0, sticky=W+E)

        # Enviamos el maximo por defecto
        self.maximo_variable.set(f"Máximo: 0")

    # Método para actualizar el máximo de elementos de la pila
    def actualizar(self, pila_informacion):
        super().actualizar(pila_informacion)

        self.maximo_variable.set(f"Máximo: {pila_informacion.get_max()}")


# Responsabilidad: Mostrar la pila en una interfaz gráfica
class PilaInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones de la pila para manipularla
class BotonesPila(BotonesBasicos):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
