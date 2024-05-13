
class Nodo:
    def __init__(self, elemento):
        self.data = elemento
        self.siguiente = None
        # Variable para saber si estamos buscando este nodo

    def __str__(self):
        return f"{self.data}"

    def get_data(self):
        return self.data


class Cola:
    def __init__(self, max=-1):
        self._size = 0
        self.frente = None
        self.fondo = None
        self.max = max

    def enqueue(self, elemento):

        nuevo = Nodo(elemento)

        # 2 - visitar el nodo
        # 3 - consultar si la cola esta vacia
        if self.frente is None and self.fondo is None:
            # 3.1  Frente y fondo apuntan a nuevo
            self.frente = nuevo
            self.fondo = nuevo

        elif self._size == self.max:
            raise Exception('No hay espacio, DESBORDAMIENTO DE PILA')

        else:
            self.fondo.siguiente = nuevo
            self.fondo = nuevo
            # 4 - actualizar datos
        self._size += 1

    def to_list(self, references=False):
        aux = self.frente
        elementos = []
        elementos_ref = []
        while True:
            if aux is None:
                break
            else:
                if type(aux.data) == str:
                    if aux.data.isdigit():
                        elementos.append(int(aux.data))

                    if not aux.data.isdigit():
                        elementos.append(aux.data)

                if not type(aux.data) == str:
                    elementos.append(aux.data)

                elementos_ref.append(aux)
                aux = aux.siguiente

        if references:
            return elementos_ref

        return elementos

    def search(self, elemento):
        aux = self.frente
        vistos = 0
        while vistos < self._size:
            if elemento == aux.data:
                return aux.data
            else:
                aux = aux.siguiente
            vistos += 1

        if vistos == self._size:
            raise Exception('Error, el elemento no existe')

    # Método que devuelve el nodo en un índice
    def search_position_node(self, index):
        if index < 0 or index >= self._size:
            raise Exception('Index out of range')
        aux = self.frente
        for i in range(index):
            aux = aux.siguiente
        return aux

    def dequeue(self):
        # 1- crear el auxiliar (señalar al frente)
        aux = self.frente

        if self._size == 0:
            raise Exception('SUBDESBORDAMIENTO DE COLA')
        elif self._size == 1:
            self.frente = None
            self.fondo = None
        else:
            # 2- Mover al frente al siguiente elemento 
            self.frente = aux.siguiente

            # 3- quitar enlaces
            aux.siguiente = None

        # 4- disminuir tamaño
        self._size -= 1

        # 5- devolver el nodo eliminado
        return aux

    def is_digit(self, value):
        if type(value) == str:
            if value.isdigit():
                return True
            else:
                return False

    def __str__(self):
        return f"Tamaño: {self._size}\nMax: {self.max}\nFrente: {self.frente}\nFondo: {self.fondo}"

    def get_size(self):
        return self._size

    def get_max(self):
        return self.max

    def get_head(self):
        return self.frente.data if self.frente is not None else None

    def get_tail(self):
        return self.fondo.data if self.fondo is not None else None

    # Método que borra la pila
    def clear(self):
        self.frente = None
        self.fondo = None
        self._size = 0
        self.max = -1
