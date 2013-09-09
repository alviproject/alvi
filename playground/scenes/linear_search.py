import random
from playground.spaces import Cartesian


class LinearSearch(object):
    Space = Cartesian

    def __init__(self, n):
        self.n = n

    def generate_points(self, space):
        for i in range(self.n):
            x = random.randint(1, self.n)
            y = i + 1
            space.create_point(x, y)

    def run(self, space):
        self.generate_points(space)
        space.sync(1)

        wanted = space.points[random.randint(0, len(space.points)-1)]
        space.create_marker("wanted", wanted)
        seeker = space.create_marker("seeker", space.points[0])
        space.sync(1)
        for point in space.points:
            seeker.move(point)
            space.sync(1)
            if wanted.id == point.id:
                break
        space.sync(1)