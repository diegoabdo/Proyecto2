# Clase que será la plantilla para todas las listas
# Contendrá las operaciones básicas de una lista, cada lista agregará sus propias funcionalidades adicionales
from tkinter import *


class EstructuraInterfaz(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.lista_frames = []

        # Configuraciones de la ventana
        self.config(width=1000, height=350, bg="#146356")
        self.grid_propagate(False)

        self.rowconfigure(0, weight=1)
    
    def actualizar(self, informacion_estructura, direccion="Horizontal"):
        self.dibujar_estructura(informacion_estructura, direccion)

    def dibujar_estructura(self, informacion_estructura, direccion):

        lista_nodos = informacion_estructura.get_list_nodes()
        nodo_buscado = informacion_estructura.get_selected_node()

        # Eliminamos los frames de la lista
        for frame in self.lista_frames:
            frame.destroy()

        # Limpiamos la lista de frames
        self.lista_frames.clear()

        # Bandera para saber si se encontró el nodo buscado
        buscado = False

        # Creamos un scrollbar para dezplazarnos a la derecha
        # Y otro para desplazarnos hacia arriba
        # Por cada nodo de la lista, se crea un frame
        for i in range(len(lista_nodos)):

            nuevo_frame = Frame(self, width=50, height=50, bg='#141E27', highlightbackground="black",
                                highlightthickness=1)

            self.lista_frames.append(nuevo_frame)

            # Se agrega el texto y la referencia del nodo al frame
            texto = Label(nuevo_frame, text=lista_nodos[i].get_data(), bg='#141E27', fg='white',
                          font=('Arial', 20))
            referencia = Label(nuevo_frame, text=lista_nodos[i].get_id(), bg='#141E27', fg='white',
                               font=('Arial', 10))

            # Comprobamos si estamos en el primer nodo
            if i == 0:
                nuevo_frame.config(bg='#003638')
                texto.config(bg='#003638')
                referencia.config(bg='#003638')

            # Comprobamos si estamos en el último nodo
            if i == len(lista_nodos) - 1:
                nuevo_frame.config(bg='#006778')
                texto.config(bg='#006778')
                referencia.config(bg='#006778')

            # Comprobamos si el nodo es el que estamos buscando
            if lista_nodos[i].get_data() == nodo_buscado and not buscado:
                nuevo_frame.config(bg='#541212')
                texto.config(bg='#541212')
                referencia.config(bg='#541212')

                buscado = True

            # Los empaquetamos
            texto.grid(row=0, column=0)
            referencia.grid(row=1, column=0)

        # Cuando tenemos más de 6 nodos, se agrega una barra de desplazamiento
        if direccion == "Horizontal":
            # Posicionamos los frames en el medio de la ventana, uno a la derecha del otro
            for i in range(len(self.lista_frames)):
                self.lista_frames[i].grid(row=0, column=i, sticky=W)

        elif direccion == "Vertical":
            self.columnconfigure(0, weight=1)
            # Posicionamos los frames en el medio de la ventana, uno debajo del otro
            for i in range(len(self.lista_frames)):
                self.lista_frames[i].grid(row=i, column=0, sticky=S)
