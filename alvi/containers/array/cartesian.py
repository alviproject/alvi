from . import base
from ..base import action


class Cartesian(base.Array):
    #TODO template value could be generated
    template = 'spaces/cartesian.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._next_x = 0

    @action('update_point')
    def update_node(self, id, value):
        return dict(id=id, y=value)

    @action('create_point')
    def create_node(self, id, value):
        self._next_x += 1
        return dict(id=id, x=self._next_x, y=value)

    @action
    def create_marker(self, id, name, node_id):
        return dict(id=id, name=name, point_id=node_id)

    @action
    def move_marker(self, id, node_id):
        return dict(id=id, point_id=node_id)

    @action
    def remove_marker(self, **kwargs):
        return kwargs