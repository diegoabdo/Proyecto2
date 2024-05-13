
# Responsabiliddad: Informar al modelo de los cambios en los controles
class ListaControllerTemplate:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    # Métodos comunes las estructuras
    def insertar_inicio(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_inicio(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def insertar_final(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_final(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar_inicio(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_inicio()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar_final(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_final()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    # Operaciones que se realizarán con el Json
    def buscar(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.buscar(valor)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def guardar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.guardar(nombre)
            self.view.actualizar_caja_opciones(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def cargar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.cargar(nombre)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def eliminar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar(nombre)
            self.view.actualizar_caja_opciones(informacion_lista)

        except Exception as e:
            print("Error: ", e)

    def cargar_opciones(self):
        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.cargar_opciones()
            self.view.actualizar_caja_opciones(informacion_lista)

        except Exception as e:
            print("Error: ", e)