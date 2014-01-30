from . import base
import alvi.client.api.cartesian as cartesian


import logging
log = logging.getLogger(__package__)


class Point(base.Item):
    def __init__(self, container, coordinates):
        super().__init__(container)
        self._value = coordinates
        cartesian.create_point(self._container._pipe, self.id, self.value.x, self.value.y)

    @property
    def value(self):
        return self._value

    @property
    def x(self):
        return self._value.x

    @property
    def y(self):
        return self._value.y


class Line(base.Item):
    def __init__(self, container, point_from, point_to):
        super().__init__(container)
        self._point_from = point_from
        self._point_to = point_to
        cartesian.create_line(self._container._pipe, self.id, self._point_from.id, self.point_to.id)

    @property
    def point_from(self):
        return self._point_from

    @point_from.setter
    def point_from(self, value):
        self._point_from = value
        cartesian.update_line(self._container._pipe, self.id, self._point_from.id, self.point_to.id)

    @property
    def point_to(self):
        return self._point_to

    @point_to.setter
    def point_to(self, value):
        self._point_to = value
        cartesian.update_line(self._container._pipe, self.id, self._point_from.id, self.point_to.id)


class Cartesian(base.Container):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._points = []

    def create_point(self, coordinates):
        self._points.append(Point(self, coordinates))

