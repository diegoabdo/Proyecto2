from tkinter import *
from tkinter import ttk


class ArbolInformacion(Frame):
    def __init__(self, master, controlador):
        super().__init__(master)

        self.controlador = controlador

        # Configuración del frame
        self.config(width=200, height=350, bg="#1A3C40")
        self.grid_propagate(False)

        # Variables camibiantes de los label
        self.raiz_variable = StringVar(self)
        self.tamanio_variable = StringVar(self)
        self.profundidad_variable = StringVar(self)

        # Label de las variables
        self.titulo = Label(self, text="Información del árbol", bg="#1A3C40", fg="white")

        self.raiz = Label(self, textvariable=self.raiz_variable, bg="#1A3C40", fg="white")
        self.tamanio = Label(self, textvariable=self.tamanio_variable, bg="#1A3C40", fg="white")
        self.profundidad = Label(self, textvariable=self.profundidad_variable, bg="#1A3C40", fg="white")

        # --------- PARTE INFERIOR DE LA INTERFAZ DE INFORMACIÓN---------------
        self.separador = Label(self, text="", bg="#1A3C40")
        self.titulo_inferior = Label(self, text="Opciones adicionales", bg="#1A3C40", fg="white")
        self.titulo_inferior2 = Label(self, text="Seleccionar estructura", bg="#1A3C40", fg="white")
        self.caja_opciones = ttk.Combobox(self, state="readonly")
        self.estructura_campo = Entry(self, width=23)

        # Contenedor de los botones
        self.contenedor_botones = Frame(self, bg="#1A3C40")

        self.cargar_btn = Button(
            self.contenedor_botones,
            text="Cargar", command=self.cargar,
            bg="#1A3C40", fg="white"
        )

        self.guardar_btn = Button(
            self.contenedor_botones,
            text="Guardar",
            command=self.guardar,
            bg="#1A3C40", fg="white"
        )

        self.eliminar_btn = Button(
            self.contenedor_botones,
            text="Eliminar",
            command=self.eliminar,
            bg="#1A3C40", fg="white"
        )

        # Posicionamiento de los botones en el contenedor
        self.cargar_btn.grid(row=0, column=0)
        self.guardar_btn.grid(row=0, column=1)
        self.eliminar_btn.grid(row=0, column=2)

        # ----------- FIN DE LA PARTE INFERIOR DE LA INTERFAZ DE INFORMACIÓN -----------

        # Posicionamiento de los labels
        self.titulo.grid(row=0, column=0, columnspan=2, sticky=W)
        self.raiz.grid(row=1, column=0, sticky=W)
        self.tamanio.grid(row=2, column=0, sticky=W)
        self.profundidad.grid(row=3, column=0, sticky=W)

        # ---- POSICIONAMIENTO DE LOS ELEMENTOS DE LA PARTE INFERIOR DE LA INTERFAZ DE INFORMACIÓN ----
        self.separador.grid(row=4, column=0, sticky=W+E)

        self.titulo_inferior.grid(row=5, column=0, sticky=W+E)
        self.titulo_inferior2.grid(row=6, column=0, sticky=W+E)
        self.caja_opciones.grid(row=7, column=0, sticky=E)
        self.estructura_campo.grid(row=8, column=0, sticky=E)

        # Contenedor de los botones
        self.contenedor_botones.grid(row=9, column=0, sticky=E)

        # Enviamos valores por defecto
        self.raiz_variable.set("Raíz: Ninguna")
        self.tamanio_variable.set("Tamaño: 0")
        self.profundidad_variable.set("Profundidad: 0")

    def cargar(self):
        self.controlador.cargar(self.caja_opciones.get())

    def guardar(self):
        self.controlador.guardar(self.estructura_campo.get())

    def eliminar(self):
        self.controlador.remover(self.caja_opciones.get())

    # Método para actualizar toda la información del árbol
    def actualizar(self, arbol_info):
        self.raiz_variable.set(f"Raíz: {arbol_info.get_root()}")
        self.tamanio_variable.set(f"Tamaño: {arbol_info.get_cantidad_nodos()}")
        self.profundidad_variable.set(f"Profundidad: {arbol_info.get_profundidad()}")

    def actualizar_caja_opciones(self, opciones):
        self.caja_opciones.config(values=opciones)

        # Comprobamos si la lista contiene alguna opción
        if opciones:
            self.caja_opciones.set(opciones[0])

        else:
            self.caja_opciones.set("")
