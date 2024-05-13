class EstructuraLinealInformacion:
    def __init__(self, head, tail, size, max_size=None, selected_node=None):
        self.head = head
        self.tail = tail
        self.size = size
        self.max_size = max_size
        self.list_nodes: [NodoInformacion] = []

        self.selected_node = selected_node

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_size(self):
        return self.size

    def get_max(self):
        return self.max_size

    def get_list_nodes(self):
        return self.list_nodes

    def set_list_nodes(self, list_nodes):
        self.list_nodes = list_nodes

    def get_selected_node(self):
        return self.selected_node

    def set_selected_node(self, selected_node):
        self.selected_node = selected_node


class NodoInformacion:
    def __init__(self, data, id_node):
        self.data = data
        self.id = id_node

    def get_data(self):
        return self.data

    def get_id(self):
        return self.id

    def set_data(self, data):
        self.data = data

    def set_id(self, reference):
        self.id = reference
