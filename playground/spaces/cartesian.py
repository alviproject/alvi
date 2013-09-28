from .space import Space
from .space import Node


class Point(object):
    def __init__(self, space, x, y):
        self._node = Node(space)
        self._x = x
        self._y = y
        space.pipe.send('create_point', (self.id, ), dict(
            id=self.id,
            x=self.x,
            y=self.y,
        ))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._update()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._update()

    def _update(self):
        self.space.pipe.send('update_point', (self.id, ), dict(
            id=self.id,
            x=self.x,
            y=self.y,
        ))

    @property
    def id(self):
        return self._node.id

    @property
    def space(self):
        return self._node.space


class Marker(object):
    def __init__(self, space, name, point):
        self.id = space.next_marker_id()
        self._space = space
        space.pipe.send('create_marker', (self.id, ), dict(
            id=self.id,
            point_id=point.id,
            name=name,
        ))

    def move(self, point):
        self._space.pipe.send('move_marker', (self.id, ), dict(
            id=self.id,
            point_id=point.id,
        ))

    def remove(self):
        self._space.pipe.send('remove_marker', (self.id, ), dict(
            id=self.id,
        ))


class Cartesian(object):
    template = "spaces/cartesian.html"

    def __init__(self):
        self._space = Space()
        self.markers = []
        #self.stats.points = 0

    @property
    def points(self):
        return self._space.nodes

    @property
    def stats(self):
        return self._space.stats

    @property
    def pipe(self):
        return self._space.pipe

    def sync(self, level):
        self._space.sync(level)

    def next_node_id(self):
        return self._space.next_node_id()

    def next_marker_id(self):
        return len(self.markers)

    def create_point(self, id, x, y):
        return ('create_point', dict(
            id=id,
            x=x,
            y=y,
        ))

        point = Point(self, x, y)
        self.add_point(point)
        return point

    def update_point(self, id, **kwargs):
        point = dict(id=id,)
        for name, value in kwargs.items():
            point[name] = value
        return 'update_point', point

    def add_point(self, point):
        self.stats.points += 1
        self._space.add_node(point)

    def create_marker(self, id, name, point_id):
        return ('create_marker', dict(
            id=id,
            name=name,
            point_id=point_id,
        ))
        marker = Marker(self, name, point)
        self.markers.append(marker)
        return marker

    def move_marker(self, id, point_id):
        return ('move_marker', dict(
            id=id,
            point_id=point_id,
        ))

    def update_stats(self, name, value):
        return ('update_stats', dict(
            name=name,
            value=value,
        ))