from . import base
from ..base import action


class Cartesian(base.List):
    template = 'spaces/cartesian.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._next_x = 0

    @action('update_point')
    def update_node(self, id, value):
        return dict(id=id, y=value)

    @action
    def create_marker(self, id, name, item_id):
        return dict(id=id, name=name, point_id=item_id)

    @action('create_point')
    def create_node(self, id, parent_id, value):
        self._next_x += 1
        return dict(id=id, x=self._next_x, y=value)

    @action
    def move_marker(self, id, item_id):
        return dict(id=id, point_id=item_id)