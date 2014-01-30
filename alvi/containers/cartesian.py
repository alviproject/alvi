from . import base
from .base import action


class Cartesian(base.Container):
    template = 'spaces/cartesian.html'

    @classmethod
    def implementations(cls):
        return (cls, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @action
    def create_point(self, id, x, y):
        return dict(id=id, x=x, y=y)

    @action
    def create_line(self, id, id_point_from, id_point_to):
        return dict(id=id, id_point_from=id_point_from, id_point_to=id_point_to)

    @action
    def update_line(self, id, id_point_from, id_point_to):
        return dict(id=id, id_point_from=id_point_from, id_point_to=id_point_to)

    @action
    def remove_line(self, id):
        return dict(id=id)

    @action
    def create_marker(self, id, name, node_id):
        return dict(id=id, name=name, point_id=node_id)

    @action
    def move_marker(self, id, node_id):
        return dict(id=id, point_id=node_id)

    @action
    def remove_marker(self, **kwargs):
        return kwargs