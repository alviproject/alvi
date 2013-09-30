from . import base
import playground.client.api.node


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        self._edges = set()
        self.create_edge(parent, call_api=False)
        print(self._edges)

    def create_child(self, value):
        return Node(self._container, self, value)

    def create_edge(self, node, call_api=True):
        if node is None or node == self:
            return
        if self.id < node.id:
            node1 = self
            node2 = node
        else:
            node1 = node
            node2 = self
        if (node1, node2) in self._edges:
            return
        self._edges.add((node1, node2))
        node._edges.add((node1, node2))
        if call_api:
            playground.client.api.node.create_edge(self._container._pipe, node1.id, node2.id)


class Graph(base.Container):
    def create_node(self, value):
        return Node(self, None, value)