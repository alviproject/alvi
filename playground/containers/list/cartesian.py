from . import base
import playground.spaces.cartesian


class Node(base.Node):
    def __init__(self, container, value):
        super().__init__(container)
        self._point = container._space.create_point(value, container._next_node_id())

    @property
    def value(self):
        return self._point.x


class Cartesian(base.List):
    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    def create_node(self, value):
        return Node(self, value)