from . import base
import playground.spaces.cartesian


class _Node(base.Node):
    def __init__(self, container, value):
        super().__init__(container)
        self._point = container._space.create_point(container._next_node_id(), value)

    @property
    def value(self):
        return self._point.y

    @value.setter
    def value(self, value):
        self._point.y = value


class Cartesian(base.Array):
    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    def _create_node(self):
        return _Node(self, 0)