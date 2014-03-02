from . import base
import alvi.client.api.array as array


class Node(base.Item):
    def __init__(self, container):
        super().__init__(container)
        self._value = 0
        array.create_node(self._container._pipe, self.id, self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        array.update_node(self._container._pipe, self.id, self.value)


class Marker(base.Marker):
    def move(self, index):
        node = self._container._nodes[index]
        return super().move(node)


#TODO iterators, etc
class Array(base.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._nodes = []

    def init(self, size):
        if self._nodes:
            raise RuntimeError("Array was already initialized")
        for i in range(size):
            self._nodes.append(Node(self))

    def __getitem__(self, index):
        return self._nodes[index].value

    def __setitem__(self, index, value):
        self._nodes[index].value = value

    def size(self):
        return len(self._nodes)

    def create_marker(self, name, node_id):
        node = self._nodes[node_id]
        return Marker(name, node)

    def swap_nodes(self, index1, index2):
        array.swap_nodes(
            self._pipe,
            node1={'id': self._nodes[index1].id},
            node2={'id': self._nodes[index2].id}
        )
        self._nodes[index1], self._nodes[index2] = self._nodes[index2], self._nodes[index1]
