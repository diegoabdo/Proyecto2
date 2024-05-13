from __future__ import annotations
from typing import Optional, TypeVar

T = TypeVar('T')


class Node:
    def __init__(self, data: T):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

        self.buscado = False

    def set_buscado(self, buscado):
        self.buscado = buscado

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_data(self):
        return self.data


class BinarySearchTree:
    def __init__(self, data=None):
        self.__root = Node(data)

    def insert1(self, data, *args):
        subtree = self.__root if len(args) == 0 else args[0]

        if subtree.data is None:
            subtree.data = data
            return

        if data < subtree.data and data:
            if subtree.left is None:
                subtree.left = Node(data)

            else:
                self.insert1(data, subtree.left)

        elif data > subtree.data:
            if subtree.right is None:
                subtree.right = Node(data)

            else:
                self.insert1(data, subtree.right)

    # Método para insertar un nodo en el árbol de búsqueda
    def insert(self, data: T, *args) -> None:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.data is None:
                node.data = data

            elif data < node.data:
                if node.left is None:
                    node.left = Node(data)

                else:
                    self.insert(data, node.left)

            elif data > node.data:
                if node.right is None:
                    node.right = Node(data)

                else:
                    self.insert(data, node.right)

        else:
            self.__root = Node(data)

    def pre_order(self, *args) -> str:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = str(node.data) + ' ('
                result += self.pre_order(node.left) + ', '
                result += self.pre_order(node.right) + ')'

                return result

        else:
            return ''

    def in_order(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.is_leaf():
                return str(node.data)

            else:
                result = '(' + self.in_order(node.left)
                result += str(node.data)
                result += self.in_order(node.right) + ')'

                return result

    # Method that insert the root of the tree
    def insert_root(self, data):
        if self.__root.get_data() is None:
            self.__root = Node(data)

    # Método que devuelve la profundidad máxima del árbol
    def max_depth(self, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]
        current_level = args[1] if len(args) >= 1 else 1

        if node is not None:
            if node.is_leaf():
                return current_level

            else:
                left = self.max_depth(node.left, current_level + 1)
                right = self.max_depth(node.right, current_level + 1)

                return max(left, right)

        else:
            return -1

    # Convertir el árbol binario en una lista utilizando el algoritmo de Eytzi
    def to_matrix(self) -> list:
        result = []

        def to_list(node: Node, level: int) -> None:
            if node is not None:
                if level == len(result):
                    result.append([])

                result[level].append(node.data)

                to_list(node.left, level + 1)
                to_list(node.right, level + 1)

        to_list(self.__root, 0)

        return result

    # Complete el árbol binario colocando todos los nodos faltantes en el lado izquierdo
    def complete_tree(self, *args) -> None:
        node = self.__root if len(args) == 0 else args[0]
        current_level = args[1] if len(args) >= 1 else 1

        if node is not None:
            if node.is_leaf() and current_level == self.max_depth():
                return

            else:
                if node.left is None:
                    node.left = Node(None)

                if node.right is None:
                    node.right = Node(None)

                self.complete_tree(node.left, current_level + 1)
                self.complete_tree(node.right, current_level + 1)

        # Método que devuelve los nodos de un nivel
        # Método que devuelve los nodos de un nivel

    def level_nodes(self, level: int, values=False, references=False) -> list:
        self.complete_tree()
        result_references = []
        result_values = []

        def level_nodes(node: Node, level: int) -> None:
            if node is not None:
                if level == len(result_references):
                    result_references.append([])
                    result_values.append([])

                result_references[level].append(node)
                result_values[level].append(node.data)

                level_nodes(node.left, level + 1)
                level_nodes(node.right, level + 1)

        level_nodes(self.__root, 0)

        if references:
            return result_references[level]

        if values:
            return result_values[level]

    def get_root(self):
        return self.__root.data

    # Método que devuelve el número total de nodos en el árbol
    def count_nodes(self, ) -> int:

        matrix_nodes = self.to_matrix()
        list_nodes = [element for sublist in matrix_nodes for element in sublist if element is not None]

        return len(list_nodes)

    def __search(self, data: T, *args) -> Optional[Node]:
        node = self.__root if len(args) == 0 else args[0]

        if node is not None:
            if node.data == data:
                return node

            else:
                result = self.__search(data, node.left)

                if result is None:
                    result = self.__search(data, node.right)

                    return result

                else:
                    return result

        else:
            return None

    def search(self, data: T) -> Optional[Node]:
        return self.__search(data)

    def to_list(self) -> list:
        matrix_nodes = self.to_matrix()
        list_nodes = [element for sublist in matrix_nodes for element in sublist if element is not None]

        return list_nodes

    # Método que hace Null todos los nodos del árbol
    def clear(self) -> None:

        def clear_tree(node: Node) -> None:
            if node is not None:
                clear_tree(node.left)
                clear_tree(node.right)
                node.data = None

        clear_tree(self.__root)

    def get_root_reference(self) -> Node:
        return self.__root

    def get_parent(self, data, *args):
        ref = self.__root if len(args) == 0 else args[0]
        parent: Optional[Node] = None if len(args) == 0 else args[1]
        if ref is not None:
            if data < ref.data:
                result = self.get_parent(data, ref.left, ref)
                return result
            elif data > ref.data:
                return self.get_parent(data, ref.right, ref)
            else:
                return parent
        else:
            return None

    def min(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.left is None:
                return node
            else:
                return self.min(node.left)
        else:
            return None

    # def remove(self, data, *args):
    #     ref = self.__root if len(args) == 0 else args[0]
    #     parent: Optional[Node] = None if len(args) == 0 else args[1]
    #
    #     if ref is not None:
    #         if data < ref.data:
    #             return self.remove(data, ref.left, ref)
    #         elif data > ref.data:
    #             return self.remove(data, ref.right, ref)
    #         else:
    #             if ref.is_leaf():
    #                 if ref.data < parent.data:
    #                     parent.left = None
    #                     return ref
    #                 else:
    #                     parent.right = None
    #                     return ref
    #             else:
    #                 if ref.left is not None and ref.right is not None:
    #                     min_node: Optional[Node] = self.min(ref.right)
    #                     print('Min', min_node)
    #                     parent = self.get_parent(min_node.data)
    #                     if min_node.data < parent.data:
    #                         parent.left = min_node.right
    #                     else:
    #                         parent.right = min_node.right
    #                     ref.data = min_node.data
    #                 else:
    #                     child: Optional[Node] = ref.right if ref.left is None else ref.left
    #
    #                     if child.data < ref.data:
    #                         ref.left = None
    #                     else:
    #                         ref.right = None
    #
    #                     if ref.data < parent.data:
    #                         parent.left = child
    #                     else:
    #                         parent.right = child
    #     else:
    #         pass
