from . import base


class Node(base.Node):
    def create_child(self, value):
        return Node(self._container, self, value)


class Graph(base.Container):
    def create_node(self, value):
        return Node(self, None, value)