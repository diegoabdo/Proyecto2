from tkinter import *


class BotonesArbol(Frame):
    def __init__(self, master, controlador):
        Frame.__init__(self, master)

        self.controlador = controlador

        # Elementos del frame
        self.dato_label = Label(self, text="Valor: ")
        self.dato_entry = Entry(self)

        self.eliminar = Button(self, text="Eliminar", command=self.eliminar)
        self.buscar = Button(self, text="Buscar", command=self.buscar)

        self.insertar_raiz = Button(self, text="Insertar raiz", command=self.insertar_raiz)
    
    def eliminar(self):
        self.controlador.eliminar(self.dato_entry.get())
        
    def buscar(self):
        self.controlador.buscar(self.dato_entry.get())

    def insertar_raiz(self):
        self.controlador.insertar_raiz(self.dato_entry.get())
