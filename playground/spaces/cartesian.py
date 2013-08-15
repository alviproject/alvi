from node import Node
import time


class Point(Node):
    def __init__(self, x, y=None):
        Node.__init__(self)
        self.x = x
        self.y = y if y else self.id + 1


class Cartesian(object):
    template = "spaces/cartesian.html"

    def __init__(self, queue):
        self.queue = queue
        self.points = []

    def create_point(self, x, y):
        point = Point(x, y)
        self.add_point(point)
        return point

    def add_point(self, point):
        action = dict(
            type='create_point',
            id=point.id,
            x=point.x,
            y=point.y,
        )
        self.points.append(point)
        self.queue.put(action)

    def update_point(self, point):
        action = dict(
            type='update_point',
            id=point.id,
            x=point.x,
            y=point.y,
        )
        self.queue.put(action)
        return point

    def swap_x(self, point_a, point_b):
        tmp = point_a.x
        point_a.x = point_b.x
        point_b.x = tmp
        self.update_point(point_a)
        self.update_point(point_b)
        time.sleep(1)