from . import base
import playground.spaces.cartesian


class Node(base.Node):
    def __init__(self, container, value):
        super().__init__(container)
        self._point = container._space.create_point(container._next_node_id(), value)

    def create_child(self, value):
        self._next = Node(self._container, value)
        return self._next

    @property
    def value(self):
        return self._point.y


class Cartesian(base.List):
    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    def create_head(self, value):
        if self.head:
            raise RuntimeError("Cannot set head more that once")
        self._head = Node(self, value)
        return self._head