from . import base
from ..base import action
import playground.spaces.cartesian


class Cartesian(base.List):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._next_x = 0

    @classmethod
    def space_class(cls):
        return playground.spaces.cartesian.Cartesian

    @action
    def create_node(self, id, parent_id, value):
        self._next_x += 1
        return self._space.create_point(id, self._next_x, value)

    @action
    def update_node(self, id, value):
        return self._space.update_point(id, y=value)

    @action
    def create_marker(self, id, name, item_id):
        return self._space.create_marker(id, name, item_id)

    @action
    def move_marker(self, id, item_id):
        return self._space.move_marker(id, item_id)