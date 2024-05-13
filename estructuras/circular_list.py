from typing import Optional, TypeVar
T = TypeVar('T')


class Node:
    def __init__(self, data):
        self.data: T = data
        self.next: Optional[Node] = None

    def get_data(self) -> T:
        return self.data


class CircularList:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def rotate_left(self) -> Node:
        if self.is_empty():
            raise Exception('Empty List')

        else:
            aux = self._head
            self._tail = self._head
            self._head = self._head.next

            return aux

    # Método que gira la lista a la derecha
    def rotate_right(self):
        if self.is_empty():
            raise Exception('Empty List')

        else:
            self._head = self._tail
            anterior = self.search_position_node(self._size - 1)
            self._tail = anterior

    def remove_head(self) -> Node:
        aux = self._head

        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            aux = self._head
            self._head = self._head.next
            self._tail.next = self._head
            aux.next = None

        self._size -= 1
        return aux

    def remove_tail(self) -> Node:
        aux = self._tail

        if self.is_empty():
            raise Exception('Subdesbordamiento')

        elif self._head == self._tail:
            self._head = None
            self._tail = None

        else:
            aux = self._tail
            precedent = self.search_position_node(self._size - 2)

            precedent.next = self._head
            self._tail.next = None
            self._tail = precedent

        self._size -= 1
        return aux

    def remove(self, data: T) -> Node:
        aux = self._search(data)

        if aux == self._head:
            self.remove_head()

        elif aux == self._tail:
            self.remove_tail()

        else:
            position = self._search_positon(aux.data)
            precedent = self.search_position_node(position - 1)

            precedent.next = aux.next
            aux.next = None

            self._size -= 1
        return aux

    def search_position_node(self, number: int) -> Node:
        aux = self._head
        iterations = 0

        while iterations <= self._size:
            if iterations is number:
                return aux

            else:
                aux = aux.next
                iterations += 1

        raise Exception('Invalid search')

    def _search_positon(self, data: T) -> int:
        aux = self._head
        iterations = 0

        while aux is not self._tail:
            if aux.data == data:
                return iterations

            else:
                aux = aux.next
                iterations += 1

        if aux.data == self._tail.data:
            return iterations

        else:
            raise Exception('Invalid search')

    # Método que busca un nodo de la lista
    def _search(self, data: T) -> Node:
        position = self._search_positon(data)
        return self.search_position_node(position)

    def search(self, data: T) -> Node:
        return self._search(data).data

    def is_empty(self) -> bool:
        return self._head is None and self._tail is None and self._size == 0

    def append(self, data) -> Node:
        new = Node(data)

        if self.is_empty():
            self._head = new
            self._tail = new
            self._tail.next = self._head

        else:
            new.next = self._head
            self._tail.next = new
            self._tail = new

        self._size += 1
        return new

    # Método que devuelve una lista de nodos
    def to_list(self, references=False):
        if self.is_empty():
            return []

        else:
            aux = self._head
            list_data = []
            list_references = []

            while aux is not self._tail:
                list_data.append(aux.data)
                list_references.append(aux)
                aux = aux.next

            list_data.append(self._tail.data)
            list_references.append(self._tail)

            if references:
                return list_references

            return list_data

    def prepend(self, data):
        if self.is_empty():
            new_node = Node(data)
            self._head = new_node
            self._tail = new_node
            self._tail.next = self._head
            self._size += 1
        else:
            new_node = Node(data)
            new_node.next = self._head
            self._head = new_node
            self._tail.next = self._head
            self._size += 1

    def traversal(self) -> str:
        result = ''
        aux = self._head
        while aux is not self._tail:
            result += str(aux.data) + ' -> '
            aux = aux.next
        result += str(self._tail.data)
        return result

    def get_size(self):
        return self._size

    def get_head(self):
        return self._head.data if self._head is not None else None

    def get_tail(self):
        return self._tail.data if self._tail is not None else None

    def clear(self):
        self._head = None
        self._tail = None
        self._size = 0