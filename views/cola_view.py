from tkinter import *
from estructuras.cola import Cola
from models.cola_model import ColaModel
from controllers.cola_controller import ColaController
from .templates.inf_estructura_template import EstructuraInformacion
from .templates.estructura_lineal_template import EstructuraInterfaz
from .templates.botones_lineales_template import BotonesBasicos


# Responsabilidad: Posicionar y mostrar todos los elementos de la interfaz
class ColaView(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Estructura de dato Cola")

        # Estructura de dato que se utilizará en el programa
        self.cola = Cola()

        # Definimos el modelo de datos
        self.modelo = ColaModel(self.cola)

        # Definimos el controlador de datos
        self.controlador = ColaController(self.modelo, self)

        # Atributos
        self.titulo = Label(self, text="Estructura de dato Cola")
        self.cola_informacion = ColaInformacion(self, self.controlador)
        self.cola_interfaz = ColaInterfaz(self)
        self.botones_inferiores = BotonesCola(self, self.controlador)

        # Posicionamiento de los elementos
        self.titulo.grid(row=0, column=0)
        self.cola_interfaz.grid(row=1, column=0)
        self.cola_informacion.grid(row=1, column=1)
        self.botones_inferiores.grid(row=2, column=0)

        self.controlador.cargar_opciones()

    # Método para actualizar toda la información de la vista
    def actualizar(self, cola_informacion):

        self.cola_informacion.actualizar(cola_informacion)
        self.cola_interfaz.actualizar(cola_informacion)

    def actualizar_caja_opciones(self, opciones):
        self.cola_informacion.actualizar_caja_opciones(opciones)


# Responsabilidad: Mostrar toda la información de la estructura de datos
class ColaInformacion(EstructuraInformacion):

    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        self.maximo_variable = StringVar(self)

        # Máximo de elementos de la pila
        self.maximo = Label(self, textvariable=self.maximo_variable, bg="#1A3C40", fg="white")
        self.maximo.grid(row=1, column=0, sticky=W + E)

        # Enviamos el maximo por defecto
        self.maximo_variable.set(f"Máximo: 0")

    def actualizar(self, pila_informacion):
        super().actualizar(pila_informacion)
        self.maximo_variable.set(f"Máximo: {pila_informacion.get_max()}")


# Responsabilidad: Mostrar la cola en una interfaz gráfica
class ColaInterfaz(EstructuraInterfaz):

    def __init__(self, master):
        super().__init__(master)


# Responsabilidad: Manejar los botones para manipular la cola
class BotonesCola(BotonesBasicos):
    def __init__(self, master, controlador):
        super().__init__(master, controlador)

        # Posicionamiento de los elementos del frame
        self.dato_label.grid(row=0, column=0)
        self.dato_entry.grid(row=0, column=1)

        self.insertar_button.grid(row=0, column=2)
        self.eliminar_button.grid(row=0, column=3)
        self.buscar_button.grid(row=0, column=4)
