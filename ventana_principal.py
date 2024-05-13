from tkinter import *

from views.arbol_binario_view import ArbolBinarioView
from views.arbol_busqueda_view import ArbolBusquedaView
from views.cola_view import ColaView
from views.lista_circular_view import ListaCircularView
from views.lista_dob_enlazada_view import ListaDobEnView
from views.lista_view import ListaView
from views.pila_view import PilaView


class Ventana(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        # El usuario tendrá 7 opciones a elegir correspondientes a las 7 estructuras
        master.title("Estructuras de Datos")
        master.geometry("400x300")
        master.config(bg="#066163")

        self.config(bg="#066163")

        # Elementos de la ventana principal

        # Textos de la ventana principal
        self.titulo = Label(self, text="Selecciona la estructura deseada",
                            font=("rockwell", 15), bg="#066163", fg="white")

        # Elementos del frame
        # Botón iniciar el frame del árbol
        self.arbol_boton = Button(
            self,
            text="Arbol",
            command=lambda: self.renderizar(ArbolBinarioView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame del arbol de busqueda
        self.arbol_busqueda_boton = Button(
            self, text="Arbol de Busqueda",
            command=lambda: self.renderizar(ArbolBusquedaView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame de cola
        self.cola_boton = Button(
            self, text="Cola",
            command=lambda: self.renderizar(ColaView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame de la lista circular
        self.lista_circular = Button(
            self, text="Lista Circular",
            command=lambda: self.renderizar(ListaCircularView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame de la lista doblemente enlazada
        self.lista_doble = Button(
            self,
            text="Lista Doble",
            command=lambda: self.renderizar(ListaDobEnView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame de la lista simplemente enlazada
        self.lista_simple = Button(
            self, text="Lista Simple",
            command=lambda: self.renderizar(ListaView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Botón iniciar el frame de la pila
        self.pila_boton = Button(
            self, text="Pila",
            command=lambda: self.renderizar(PilaView),

            # Estilos
            bg="#383838",
            width=20,
            height=1,
            font=("rockwell", 12),
            fg="white"
        )

        # Posicionamos todos los elementos
        self.titulo.grid(row=0, column=0)

        self.arbol_boton.grid(row=1, column=0)
        self.arbol_busqueda_boton.grid(row=2, column=0)
        self.cola_boton.grid(row=3, column=0)
        self.lista_circular.grid(row=4, column=0)
        self.lista_doble.grid(row=5, column=0)
        self.lista_simple.grid(row=6, column=0)
        self.pila_boton.grid(row=7, column=0)

    def renderizar(self, view):

        root = Toplevel()

        ventana_view = view(root)
        ventana_view.pack()

        root.mainloop()