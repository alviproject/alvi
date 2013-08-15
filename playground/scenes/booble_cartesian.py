import random
from playground.spaces import Cartesian
import time


class BoobleCartesian(object):
    def __init__(self, n):
        self.n = n
        self.Space = Cartesian

    def generate_points(self, space):
        """ generates n points (x, y) on a given space
            x is generated randomly (values 1-n)
            y is just incremented, the reason is that it looks better; thanks to that, when you swap adjacent elements
            (with adjacent ids) user can see that adjacent circles (with adjacent y values) are swapped
        """
        points = [] #TODO
        for i in xrange(self.n):
            x = random.randint(1, self.n)
            y = i + 1
            point = space.create_point(x, y)
            points.append(point)
        return points

    def run(self, space):
        space.stats.comparisons = 0
        space.stats.assignments = 0
        points = self.generate_points(space)

        changed = True
        while changed:
            changed = False
            for j in xrange(1, len(points)):
                point_a = points[j]
                point_b = points[j-1]

                space.stats.comparisons += 1
                if point_a.x > point_b.x:
                    tmp = point_a.x
                    point_a.x = point_b.x
                    point_b.x = tmp
                    space.stats.assignments += 2
                    space.update_point(point_a)
                    space.update_point(point_b)
                    time.sleep(1)
                    changed = True
