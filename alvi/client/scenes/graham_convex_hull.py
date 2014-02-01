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
Vector = Coordinates
PointWithDetails = collections.namedtuple('PointWithDetails', 'point angle distance')


def angle(p0, p1):
    p0_to_p1 = Vector(p1.x - p0.x, p1.y - p0.y)
    len_b = math.sqrt(p0_to_p1.x**2 + p0_to_p1.y**2)
    #derived from dot product definition - the second vector is (1, 0)
    cos_ = p0_to_p1.x / len_b
    return -cos_


def distance(p0, p1):
    section = Vector(p1.x - p0.x, p1.y - p0.y)
    return math.sqrt(section.x**2 + section.y**2)


def cross_product(p0, p1, p2):
    return ((p1.x-p0.x)*(p2.y-p0.y)) - ((p2.x-p0.x)*(p1.y - p0.y))


class LineStack():

    def __init__(self, container):
        self.container = container
        self.points = []
        self._popped_since_last_sync = 0
        self._lines = []

    def pop(self):
        self.points.pop()
        self._popped_since_last_sync += 1

    def push(self, point):
        self.points.append(point)
        if len(self.points) > 1:
            self._sync_after_push()

    def _sync_after_push(self):
        if self._popped_since_last_sync == 0:
            self._lines.append(Line(self.container, self.points[-2], self.points[-1]))
        elif self._popped_since_last_sync == 1:
            self._lines[-1].point_to = self.points[-1]
            self._popped_since_last_sync = 0
        else:
            for i in range(self._popped_since_last_sync-1):
                cartesian.remove_line(self.container._pipe,  self._lines.pop().id)
                self.container.sync()
            self._lines[-1].point_to = self.points[-1]
            self._popped_since_last_sync = 0
        self.container.sync()


class GrahamConvexHull(base.Scene):
    def run(self, **kwargs):
        container = kwargs['container']
        data_generator = kwargs['data_generator']
        self.generate_nodes(container, data_generator)
        self.find_convex_hull(container)

    def generate_nodes(self, container, data_generator):
        #create a set of unique 2d points
        all_points = [Coordinates(*xy) for xy in itertools.product(range(1, 46), range(1, 16))]
        random.shuffle(all_points)
        for point in all_points[:45]:
            container.create_point(point)
        container.sync()

    def find_convex_hull(self, container):
        lowest_leftmost_point, rest_points = self.find_lowest_leftmost(container.points)
        rest_points = self.sort_by_angle_from_lowest(lowest_leftmost_point, rest_points)
        rest_points = self.remove_points_with_same_angle(rest_points)

        line_stack = LineStack(container)
        line_stack.push(lowest_leftmost_point)
        line_stack.push(rest_points[0].point)
        line_stack.push(rest_points[1].point)

        for point in rest_points[2:]:
            while cross_product(line_stack.points[-2], line_stack.points[-1], point.point) < 0:
                line_stack.pop()
            line_stack.push(point.point)
        line_stack.push(lowest_leftmost_point)

    def find_lowest_leftmost(self, points):
        sorted_points = sorted(points, key=operator.attrgetter('y', 'x'))
        lowest_leftmost_point = sorted_points[0]
        return lowest_leftmost_point, sorted_points[1:]

    def sort_by_angle_from_lowest(self, origin_point,  points):
        p0 = origin_point
        points_with_angles_and_distances = [
            PointWithDetails(p, angle(p0, p), distance(p0, p)) for p in points
        ]
        all_other_points = sorted(
            points_with_angles_and_distances,
            key=operator.attrgetter('angle', 'distance'))
        return all_other_points

    def remove_points_with_same_angle(self, rest_points):
        """
        Point sorted by angle and distance from origin
        - if angle is the same, leaves only the furthest one
        """
        all_other_points_unique = []
        last_point = rest_points[-1]
        all_other_points_unique.append(last_point)
        for current_point in reversed(rest_points[:-1]):
            old_angle = last_point.angle
            new_angle = current_point.angle
            if old_angle != new_angle:
                all_other_points_unique.append(current_point)
                last_point = current_point
        all_other_points_unique = list(reversed(all_other_points_unique))
        return all_other_points_unique

    @staticmethod
    def container_class():
        return alvi.client.containers.Cartesian


if __name__ == "__main__":
    GrahamConvexHull.start()