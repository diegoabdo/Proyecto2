from .templates.lista_model_template import ListaModelTemplate
from .fichero import Fichero


class ListaSimpleModel(ListaModelTemplate):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_enlazadas.json")