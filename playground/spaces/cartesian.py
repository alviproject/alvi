from space import Space
from space import Node


class Point(object):
    def __init__(self, space, x, y):
        self._node = Node(space)
        self._x = x
        self._y = y
        space.queue.put(dict(
            type='create_point',
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
        self.space.queue.put(dict(
            type='update_point',
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


class Cartesian(object):
    template = "spaces/cartesian.html"

    def __init__(self, queue):
        self._space = Space(queue)
        self.stats.points = 0

    @property
    def points(self):
        return self._space.nodes

    @property
    def stats(self):
        return self._space.stats

    @property
    def queue(self):
        return self._space.queue

    def next_node_id(self):
        return self._space.next_node_id()

    def create_point(self, x, y):
        point = Point(self, x, y)
        self.add_point(point)
        return point

    def add_point(self, point):
        self.stats.points += 1
        self._space.add_node(point)