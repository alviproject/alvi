from node import Node
import time
from space import Space


class Point(Node):
    def __init__(self, x, y=None):
        Node.__init__(self)
        self.x = x
        self.y = y if y else self.id + 1


class Cartesian(Space):
    template = "spaces/cartesian.html"

    def __init__(self, queue):
        Space.__init__(self, queue)
        self.points = []
        self.stats.points = 0

    def create_point(self, x, y):
        point = Point(x, y)
        self.add_point(point)
        return point

    def add_point(self, point):
        self.stats.points += 1
        self.points.append(point)
        self.queue.put(dict(
            type='create_point',
            id=point.id,
            x=point.x,
            y=point.y,
        ))

    def update_point(self, point):
        self.queue.put(dict(
            type='update_point',
            id=point.id,
            x=point.x,
            y=point.y,
        ))
        return point

    #TODO remove
    def swap_x(self, point_a, point_b):
        tmp = point_a.x
        point_a.x = point_b.x
        point_b.x = tmp
        self.update_point(point_a)
        self.update_point(point_b)
        time.sleep(1)