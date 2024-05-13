from .templates.lista_model_template import ListaModelTemplate
from .fichero import Fichero


class ListaDoblementeEnlazadaModel(ListaModelTemplate):
    def __init__(self, list_name):
        super().__init__(list_name)

        self.fichero = Fichero("recursos/datos/listas_dob_enlazadas.json")

    def insertar_por_indice(self, elemento, indice):
        self.list.append_in_position(elemento, indice)

        return self.obtener_informacion()

    def eliminar_por_indice(self, indice):
        self.list.remove_in_position(indice)

        return self.obtener_informacion()