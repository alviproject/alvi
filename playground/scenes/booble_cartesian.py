import random
from playground.spaces import Cartesian
import time


class BoobleCartesian(object):
    Space = Cartesian

    def __init__(self, n):
        self.n = n

    def generate_points(self, space):
        """ generates n points (x, y) on a given space
            x is generated randomly (values 1-n)
            y is just incremented, the reason is that it looks better; thanks to that, when you swap adjacent elements
            (with adjacent ids) user can see that adjacent circles (with adjacent y values) are swapped
        """
        for i in range(self.n):
            x = random.randint(1, self.n)
            y = i + 1
            space.create_point(x, y)

    def run(self, space):
        space.stats.comparisons = 0
        space.stats.assignments = 0
        self.generate_points(space)
        space.sync(1)

        changed = True
        while changed:
            changed = False
            for j in range(1, len(space.points)):
                point_a = space.points[j]
                point_b = space.points[j-1]

                space.stats.comparisons += 1
                if point_a.x > point_b.x:
                    tmp = point_a.x
                    point_a.x = point_b.x
                    point_b.x = tmp
                    space.stats.assignments += 2
                    changed = True
            space.sync(1)
