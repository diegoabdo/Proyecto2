from controllers.templates.lista_controller_template import ListaControllerTemplate


class ListaSimpleController(ListaControllerTemplate):
    def __init__(self, model, view):
        super().__init__(model, view)
