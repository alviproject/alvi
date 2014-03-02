from . import base
from ..base import action


class Cartesian(base.Array):
    template = 'spaces/cartesian.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @action('update_point')
    def update_node(self, id, value):
        return dict(id=id, y=value)

    @action('create_point')
    def create_node(self, id, value):
        return dict(id=id, x=id+1, y=value)

    @action('swap_points')
    def swap_nodes(self, **kwargs):
        return kwargs

    @action
    def create_marker(self, id, name, node_id):
        return dict(id=id, name=name, point_id=node_id)

    @action
    def move_marker(self, id, node_id):
        return dict(id=id, point_id=node_id)

    @action
    def remove_marker(self, **kwargs):
        return kwargs