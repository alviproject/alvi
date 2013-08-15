from playground import service
from playground.spaces import Cartesian
from playground.spaces import Sorting
from playground import scenes
import random
import time


N = 10  # number of points and max value of the point


def generate_points(space, n):
    """ generates n points (x, y) on a given space
        x is generated randomly (values 1-n)
        y is just incremented, the reason is that it looks better; thanks to that, when you swap adjacent elements
         (with adjacent ids) user can see that adjacent circles (with adjacent y values) are swapped
    """
    points = []
    for i in xrange(n):
        x = random.randint(1, n)
        y = i + 1
        point = space.create_point(x, y)
        points.append(point)
    return points


def booble(queue):
    space = Cartesian(queue)
    space.stats.comparisons = 0
    space.stats.assignments = 0
    points = generate_points(space, N)

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


@scenes.register(Sorting)
class Booble2(object):
    def run(self, queue):
        self.space.stats.test = 0
        for i in xrange(N):
            self.space.create_item(random.randint(1, N))

        changed = True
        while changed:
            changed = False
            for j in xrange(1, len(self.space.items)):
                item_a = self.space.items[j]
                item_b = self.space.items[j-1]

                self.space.stats.test += 1
                if item_a > item_b:
                    self.space.swap(item_a, item_b)
                    changed = True


#service.add_scene("Booble Sort", booble, Cartesian)
#service.add_scene("Booble 2", booble2, Sorting)
service.run()
