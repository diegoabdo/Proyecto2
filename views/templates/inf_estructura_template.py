# Clase que almacenará una estructura y que contendrá todos sus atributos
from tkinter import *
from tkinter import ttk


class EstructuraInformacion(Frame):
    def __init__(self, master, controlador):
        Frame.__init__(self, master)

        self.controlador = controlador

        # Variables cambiantes de los label
        self.tamanio_variable = StringVar(self)
        self.tope_variable = StringVar(self)
        self.fondo_variable = StringVar(self)

        self.config(bg="#1A3C40", width=200, height=350)
        self.grid_propagate(False)

        # Elementos del frame
        self.titulo = Label(self, text="Información de la estructura")

        self.tamanio = Label(self, textvariable=self.tamanio_variable)
        self.tope = Label(self, textvariable=self.tope_variable)
        self.fondo = Label(self, textvariable=self.fondo_variable)

        # Parte baja de las opciones
        self.separador = Label(self, text="", bg="darkred")
        self.titulo_inferior = Label(self, text="Opciones adicionales")
        self.titulo_inferior2 = Label(self, text="Seleccionar estructura")
        self.caja_opciones = ttk.Combobox(self, state="readonly")
        self.estructura_campo = Entry(self, width=23)

        # Contenedor de los botones
        self.contenedor_botones = Frame(self, bg="darkred")

        self.cargar_btn = Button(self.contenedor_botones, text="Cargar", command=self.cargar)
        self.guardar_btn = Button(self.contenedor_botones, text="Guardar", command=self.guardar)
        self.eliminar_btn = Button(self.contenedor_botones, text="Eliminar", command=self.eliminar)

        # Posicionamiento de los botones en el contenedor
        self.cargar_btn.grid(row=0, column=0)
        self.guardar_btn.grid(row=0, column=1)
        self.eliminar_btn.grid(row=0, column=2)

        # Aplicamos estilos a los elementos
        self.aplicar_estilo(self.titulo)
        self.aplicar_estilo(self.tamanio)
        self.aplicar_estilo(self.tope)
        self.aplicar_estilo(self.fondo)
        self.aplicar_estilo(self.separador)
        self.aplicar_estilo(self.titulo_inferior)
        self.aplicar_estilo(self.titulo_inferior2)
        self.aplicar_estilo(self.cargar_btn)
        self.aplicar_estilo(self.guardar_btn)
        self.aplicar_estilo(self.eliminar_btn)

        self.titulo.config(font=("Arial", 10))
        self.titulo_inferior.config(font=("Arial", 10))

        # Posicionamiento de los elementos en el frame
        self.titulo.grid(row=0, column=0, sticky=E)
        self.tamanio.grid(row=2, column=0, sticky=W + E)
        self.tope.grid(row=3, column=0, sticky=W + E)
        self.fondo.grid(row=4, column=0, sticky=W + E)

        # Parte inferior de la información
        self.separador.grid(row=5, column=0, sticky=W + E)

        self.titulo_inferior.grid(row=6, column=0, sticky=W + E)
        self.titulo_inferior2.grid(row=7, column=0, sticky=W + E)
        self.caja_opciones.grid(row=8, column=0, sticky=E)
        self.estructura_campo.grid(row=9, column=0, sticky=E)

        # Botones
        self.contenedor_botones.grid(row=10, column=0, sticky=E)

        # Enviamos valores por defecto
        self.tamanio_variable.set(f"Tamaño: 0")
        self.tope_variable.set("Tope: Ninguno")
        self.fondo_variable.set("Fondo: Ninguno")

    # Método para guardar la estructura
    def guardar(self):
        self.controlador.guardar(self.estructura_campo.get())

    def cargar(self):
        self.controlador.cargar(self.caja_opciones.get())

    def eliminar(self):
        self.controlador.eliminar(self.caja_opciones.get())

    # Método para aplicar estilo a todos los elementos
    def aplicar_estilo(self, elemento):
        elemento.config(bg="#1A3C40", fg="white")

    # Método para actualizar toda la información común de la estructura
    def actualizar(self, estructura_informacion):
        self.tamanio_variable.set(f"Tamaño: {estructura_informacion.get_size()}")
        self.tope_variable.set(f"Tope: {estructura_informacion.get_head()}")
        self.fondo_variable.set(f"Fondo: {estructura_informacion.get_tail()}")

    # Método para actualizar la caja de opciones
    def actualizar_caja_opciones(self, lista_opciones):
        self.caja_opciones.config(values=lista_opciones)

        # Comprobamos que la list no esté vacía
        if lista_opciones:
            self.caja_opciones.set(lista_opciones[0])

        # En caso de estar vacía
        if not lista_opciones:
            self.caja_opciones.set('')
