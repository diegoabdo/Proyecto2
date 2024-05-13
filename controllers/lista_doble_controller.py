from .templates.lista_controller_template import ListaControllerTemplate


class ListaDobEnlazadaController(ListaControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)

    def insertar_por_indice(self, dato, indice):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.insertar_por_indice(dato, indice)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)

    def eliminar_por_indice(self, indice):

        try:
            # Intentamos mostrar la información
            informacion_lista = self.model.eliminar_por_indice(indice)
            self.view.actualizar(informacion_lista)

        except Exception as e:
            print(e)
