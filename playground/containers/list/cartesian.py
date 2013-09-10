from . import base
import playground.spaces.cartesian


class Node(base.Node):
    def __init__(self, container, point, value):
        super().__init__(container)
        self._point = point

    @property
    def value(self):
        return self._point.x


class Cartesian(base.List):
    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    def create_node(self, value):
        point = self._space.create_point(value, self._next_node_id())
        node = Node(self, point, value)
        self._nodes.append(node)
        return node