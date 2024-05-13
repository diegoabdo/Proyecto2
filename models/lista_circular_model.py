from .templates.lista_model_template import ListaModelTemplate
from .fichero import Fichero


class ListaCircularModel(ListaModelTemplate):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_circulares.json")

    def rotar_izquierda(self):
        self.list.rotate_left()

        return self.obtener_informacion()

    def rotar_derecha(self):
        self.list.rotate_right()

        return self.obtener_informacion()