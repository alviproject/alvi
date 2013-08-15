from playground import service
from playground.spaces import Cartesian
from playground.spaces import Sorting
import random


N = 100  # number of points and max value of the point


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
    points = generate_points(space, N)

    changed = True
    while changed:
        changed = False
        for j in xrange(1, len(points)):
            point_a = points[j]
            point_b = points[j-1]

            if point_a.x > point_b.x:
                space.swap_x(point_a, point_b)
                changed = True


def booble2(queue):
    space = Sorting(queue)
    for i in xrange(N):
        space.create_item(random.randint(1, N))

    changed = True
    while changed:
        changed = False
        for j in xrange(1, len(space.items)):
            item_a = space.items[j]
            item_b = space.items[j-1]

            if item_a > item_b:
                space.swap(item_a, item_b)
                changed = True


service.add_scene("Booble Sort", booble, Cartesian)
service.add_scene("Booble 2", booble2, Sorting)
service.run()