from .templates.lista_controller_template import ListaControllerTemplate


class ListaCircualarController(ListaControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)

    def rotar_izquierda(self):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.rotar_izquierda()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)

    def rotar_derecha(self):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.rotar_derecha()
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)
