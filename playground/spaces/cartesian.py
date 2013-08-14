from node import Node
import time


class Point(Node):
    def __init__(self, x, y):
        Node.__init__(self)
        self.x = x
        self.y = y


class Cartesian(object):
    template = "spaces/cartesian.html"

    def __init__(self, queue):
        self.queue = queue

    def create_point(self, x, y):
        point = Point(x, y)
        action = dict(
            type='create_point',
            id=point.id,
            x=point.x,
            y=point.y,
        )
        self.queue.put(action)
        return point

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