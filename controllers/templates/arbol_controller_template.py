

# Responsabiliddad: Informar al modelo de los cambios en los controles
class ArbolBinarioControllerTemplate:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def insertar_raiz(self, dato):
        try:
            informacion_arbol = self.model.insertar_raiz(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def buscar(self, dato):
        try:
            informacion_arbol = self.model.buscar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    def eliminar(self, dato):
        try:
            informacion_arbol = self.model.eliminar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)

    # ------- OPERACIONES CON EL FICHERO PARA ALMACENAR INFORMACIÓN DEL ÁRBOL -------
    def guardar(self, nombre):
        try:
            opciones = self.model.guardar(nombre)
            self.view.actualizar_caja_opciones(opciones)

        except Exception as e:
            print("Error: ", e)

    def cargar(self, nombre):
        try:
            informacion_arbol = self.model.cargar(nombre)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error: ", e)

    def remover(self, nombre):
        try:
            opciones = self.model.remover(nombre)
            self.view.actualizar_caja_opciones(opciones)

        except Exception as e:
            print("Error: ", e)

    def cargar_opciones(self):
        try:
            opciones = self.model.cargar_opciones()
            self.view.actualizar_caja_opciones(opciones)

        except Exception as e:
            print("Error: ", e)
