

# Controller for Queue
class ColaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insert(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.enqueue(valor)
            self.view.actualizar(informacion_cola)

        # En caso de una excepción, la imprimimos
        except Exception as e:
            print(e)

    def remove(self):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.dequeue()
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)

    def search(self, valor):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.search(valor)
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print(e)

    # Operaciones que se realizarán con el Json
    def guardar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.guardar(nombre)
            self.view.actualizar_caja_opciones(informacion_cola)

        except Exception as e:
            print("Error: ", e)

    def cargar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.cargar(nombre)
            self.view.actualizar(informacion_cola)

        except Exception as e:
            print("Error: ", e)

    def eliminar(self, nombre):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.eliminar(nombre)
            self.view.actualizar_caja_opciones(informacion_cola)

        except Exception as e:
            print("Error: ", e)

    def cargar_opciones(self):
        try:
            # Intentamos mostrar la información
            informacion_cola = self.model.cargar_opciones()
            self.view.actualizar_caja_opciones(informacion_cola)

        except Exception as e:
            print("Error: ", e)
