import math
import random
import itertools
import operator
import collections
import alvi.client.containers
import alvi.client.utils
from alvi.client.containers.cartesian import Line
import alvi.client.api.cartesian as cartesian
from . import base
import logging

log = logging.getLogger(__package__)
Coordinates = collections.namedtuple('Coordinates', 'x y')
PointWithDetails = collections.namedtuple('PointWithDetails', 'point angle distance')


class LineStack():

    def __init__(self, container):
        self.container = container
        self._points = []
        self._popped_since_last_sync = 0
        self._lines = []

    def pop(self):
        self._points.pop()
        self._popped_since_last_sync += 1

    def push(self, point):
        self._points.append(point)
        if len(self._points) > 1:
            self._sync_after_push()

    def _sync_after_push(self):
        if self._popped_since_last_sync == 0:
            self._lines.append(Line(self.container, self._points[-2], self._points[-1]))
        elif self._popped_since_last_sync == 1:
            self._lines[-1].point_to = self._points[-1]
            self._popped_since_last_sync = 0
        else:
            for i in range(self._popped_since_last_sync-1):
                cartesian.remove_line(self.container._pipe,  self._lines.pop().id)
                self.container.sync()
            self._lines[-1].point_to = self._points[-1]
            self._popped_since_last_sync = 0
        self.container.sync()


class GrahamConvexHull(base.Scene):

    def generate_nodes(self, container, data_generator):
        #create a set of unique 2d points
        all_points = [Coordinates(*xy) for xy in itertools.product(range(1, 46), range(1, 16))]
        random.shuffle(all_points)
        for point in all_points[:45]:
            container.create_point(point)
        container.sync()

    def find_convex_hull(self, container):
        points = container._points
        #find lowest leftmost point
        sorted_points = sorted(points, key=operator.attrgetter('y', 'x'))
        #sort all other points by angle and distance from origin, if same angle use only point that is further away
        #since p0 is lowest leftmost, we know that if it is center of polar coors system, angles will be in 0, pi range
        #so, we can use -cos as a sorting key function
        p0 = sorted_points[0]
        def calculate_angle_from_p0(p):
            a = (1, 0)
            b = (p.x - p0.x, p.y - p0.y)
            len_b = math.sqrt((b[0]**2 + b[1]**2))
            dot_product = (a[0]*b[0] + a[1]*b[1])
            cos_ = dot_product / len_b #len_a == 1
            return -cos_

        def calculate_distance_from_p0(p):
            b = (p.x - p0.x, p.y - p0.y)
            return math.sqrt((b[0]**2 + b[1]**2))

        points_with_angles_and_distances = [
            PointWithDetails(p, calculate_angle_from_p0(p), calculate_distance_from_p0(p)) for p in sorted_points[1:]
        ]

        all_other_points = sorted(points_with_angles_and_distances, key=operator.attrgetter('angle', 'distance'))

        all_other_points_unique = []
        last_point = all_other_points[-1]
        all_other_points_unique.append(last_point)
        for current_point in reversed(all_other_points[:-1]):
            old_angle = last_point.angle
            new_angle = current_point.angle
            if old_angle != new_angle:
                all_other_points_unique.append(current_point)
                last_point = current_point
        all_other_points_unique = list(reversed(all_other_points_unique))

        line_stack = LineStack(container)
        line_stack.push(p0)
        line_stack.push(all_other_points_unique[0].point)
        container.sync()
        line_stack.push(all_other_points_unique[1].point)
        container.sync()

        def cross_product(p0, p1, p2):
            return ((p1.x-p0.x)*(p2.y-p0.y)) - ((p2.x-p0.x)*(p1.y - p0.y))
        for pX in all_other_points_unique[2:]:
            while True:
                cross = cross_product(line_stack._points[-2], line_stack._points[-1], pX.point)
                if cross < 0:
                    line_stack.pop()
                else:
                    break
            line_stack.push(pX.point)
            container.sync()
        line_stack.push(p0)
        container.sync()

    def run(self, **kwargs):
        cartesian = kwargs['container']
        data_generator = kwargs['data_generator']
        self.generate_nodes(cartesian, data_generator)
        self.find_convex_hull(cartesian)

    @staticmethod
    def container_class():
        return alvi.client.containers.Cartesian


if __name__ == "__main__":
    GrahamConvexHull.start()