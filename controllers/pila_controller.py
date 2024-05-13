# Controller for Stack

class PilaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert(self, valor):

        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.push(valor)
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print("Error: ", e)

    def remove(self):
        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.pop()
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print("Error: ", e)

    def search(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_pila = self.model.search(valor)
            self.view.actualizar(informacion_pila)

        except Exception as e:
            print("Error: ", e)

    # Operaciones que se realizarán con el Json
    def guardar(self, nombre):
        try:
            # Intentamos llevar a cabo la operación
            informacion_pila = self.model.guardar(nombre)
            self.view.actualizar_pila_opciones(informacion_pila)

        except Exception as e:
            print("error: ", e)

    def cargar(self, nombre):
        try:
            # Intentamos llevar a cabo la operación
            informacion_pila = self.model.cargar(nombre)
            self.view.actualizar(informacion_pila)

        except Exception as e:
            # En caso de una excepción, la imprimimos
            print("Error: ", e)

    def eliminar(self, nombre):
        try:
            # Intentamos llevar a cabo la operación
            informacion_pila = self.model.eliminar(nombre)
            self.view.actualizar_pila_opciones(informacion_pila)

        except Exception as e:
            print("Error: ", e)

    # Método para recibir todas las estructuras de datos disponibles en el Json
    def cargar_opciones(self):
        try:
            # Intentamos llevar a cabo la operación
            informacion_pila = self.model.cargar_opciones()
            self.view.actualizar_pila_opciones(informacion_pila)

        except Exception as e:
            print("Error: ", e)
