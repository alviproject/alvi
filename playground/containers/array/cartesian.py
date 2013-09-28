from . import base
from ..base import action
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._next_x = 0

    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    def _create_node(self):
        return _Node(self, 0)

    @action
    def update_element(self, id, value):
        return self._space.update_point(id, y=value)

    @action
    def create_element(self, id, value):
        self._next_x += 1
        return self._space.create_point(id, self._next_x, value)

    @action
    def create_marker(self, id, name, node_id):
        return self._space.create_marker(id, name, node_id)

    @action
    def move_marker(self, id, node_id):
        return self._space.move_marker(id, node_id)