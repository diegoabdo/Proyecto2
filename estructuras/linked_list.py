from typing import Optional, TypeVar, Generic
T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[Node] = None

    def get_data(self) -> T:
        return self.data


# Crea una lista que solo permita nodos de un tipo de dato (genérico)
class LinkedList(Generic[T]):
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    # Método que utiliza la función len() de python para determinar el número de elementos en la estructura
    def __len__(self) -> int:
        return self._size

    # Atributo de lectura para acceder a la datos del primer nodo
    # Si no hay elementos lanza una excepción
    @property
    def first(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self._head.data

    # Atributo de lectura para acceder a la datos del último nodo
    # Si no hay elementos lanza una excepción
    @property
    def last(self) -> T:
        if self.is_empty():
            raise Exception('Linked List is empty')
        else:
            return self._tail.data

    # Método que verifica si la lista enlazada se encuentra vacía (no hay nodos)
    def is_empty(self):
        return self._head is None and self._tail is None

    # Método para recorrer todos los nodos de una lista, devuelve una cadena con toda la datos
    def traversal(self) -> str:
        result: str = ''
        current: Optional[Node] = self._head
        while current is not None:
            if current == self._tail:
                result += str(current.data)
            else:
                result += str(current.data) + '->'
            current = current.next
        return result

    # Método que busca el nodo que contenga un valor en específico
    # Devuelve la primera coincidencia
    # Si no hay nodos con ese valor, debe lanzar una excepción
    def search_node_positon(self, data):
        iterations = 0
        aux = self._head

        while aux is not None:
            if aux.data == data:
                return iterations

            else:
                iterations += 1
                aux = aux.next

        raise Exception('El elemento no existe')

    def search_position_node(self, position):
        iterations = 0
        aux = self._head

        while aux is not None:
            if position == iterations:
                return aux

            else:
                iterations += 1
                aux = aux.next

        raise Exception('Posicion inexistente')

    # Método que busca un nodo por datos
    def search(self, data):
        current = self._head
        while current is not None:
            if current.data == data:
                return current.data
            current = current.next

        return None

    # Método que devuelve una lista con todos los datos de los nodos
    def to_list(self, references=False):
        current = self._head
        result = []
        result_references = []

        while current is not None:
            result.append(current.data)
            result_references.append(current)
            current = current.next

        if references:
            return result_references

        return result

    # Método para insertar un nuevo nodo al principio de la lista
    def prepend(self, data: T) -> None:
        new_node: Node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node
        self._size += 1

    # Método que añade al final un nuevo nodo a la lista
    def append(self, data: T) -> None:
        new_node: Node = Node(data)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    # Método que elimina el primer nodo que contenga el valor pasado como parámetro
    def remove_head(self):
        aux = self._head

        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._size == 1:
            self._head = None
            self._tail = None

        else:
            self._head = aux.next
            aux.next = None

        self._size -= 1
        return aux

    # Mmétodo que quita el nodo tail
    def remove_tail(self):
        aux = self._tail

        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._size == 1:
            self._head = None
            self._tail = None

        else:
            self._tail = self.search_position_node(self._size - 2)
            self._tail.next = None

        self._size -= 1
        return aux

    def remove(self, data) -> T:
        aux = self.search(data)

        if self._head == aux:
            self.remove_head()

        elif self._tail == aux:
            self.remove_tail()

        else:
            slot = self.search_node_position(data)
            anterior = self.search_position_node(slot - 1)

            anterior.next = aux.next
            aux.next = None

        self._size -= 1
        return aux

    def get_size(self):
        return self._size
    
    def get_head(self):
        return self._head.data if self._head is not None else None

    def get_tail(self):
        return self._tail.data if self._tail is not None else None

    # Metodo que limpia la lista
    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0
