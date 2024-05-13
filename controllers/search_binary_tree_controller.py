from controllers.templates.arbol_controller_template import ArbolBinarioControllerTemplate


class ArbolBinarioBusquedaController(ArbolBinarioControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.model = model
        self.view = view

    def insertar(self, dato):
        try:
            informacion_arbol = self.model.insertar(dato)
            self.view.mostrar_arbol(informacion_arbol)

        except Exception as e:
            print("Error:", e)
