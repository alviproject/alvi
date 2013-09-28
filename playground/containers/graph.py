from . import base
from .base import action
import playground.spaces


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._node = playground.spaces.graph.Node(container._space, parent, value)

    @property
    def value(self):
        return self._node.value

    def create_child(self, value):
        return Node(self._container, self, value)


class Graph(base.Container):
    @classmethod
    def implementations(cls):
        return (cls, )

    @classmethod
    def space_class(cls):
        return playground.spaces.Graph

    @action
    def create_node(self, id, value, parent_id):
        return self._space.create_node(id, value, parent_id)