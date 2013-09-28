from . import base


class Cartesian(base.Space):
    template = "spaces/cartesian.html"

    def create_point(self, id, x, y):
        return ('create_point', dict(
            id=id,
            x=x,
            y=y,
        ))

    def update_point(self, id, **kwargs):
        point = dict(id=id,)
        for name, value in kwargs.items():
            point[name] = value
        return 'update_point', point

    def create_marker(self, id, name, point_id):
        return ('create_marker', dict(
            id=id,
            name=name,
            point_id=point_id,
        ))

    def move_marker(self, id, point_id):
        return ('move_marker', dict(
            id=id,
            point_id=point_id,
        ))

    def remove_marker(self, id):
        return ('remove_marker', dict(
            id=id,
        ))