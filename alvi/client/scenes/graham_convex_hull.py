import collections
import alvi.client.containers
import alvi.client.utils
from alvi.client.containers.cartesian import Line
from . import base

import logging
log = logging.getLogger(__package__)

Coordinates = collections.namedtuple('Coordinates', 'x y')

class GrahamConvexHull(base.Scene):

    def generate_nodes(self, container, data_generator):
        import random
        import itertools
        #create a set of unique 2d points
        all_points = [Coordinates(*xy) for xy in itertools.product(range(1, 46), range(1, 16))]
        random.shuffle(all_points)
        for point in all_points[:10]:
            container.create_point(point)

        container.sync()
        p0 = container._points[0]
        p1 = container._points[1]
        first_line = Line(container, p0, p1)
        container.sync()

        for pX in container._points[2:]:
            first_line.point_to = pX
            container.sync()

        for pX in container._points[1:-3]:
            log.info('draw_line %s, %s' % (p0, pX))
            Line(container, p0, pX)
            container.sync()

        container.sync()

    def run(self, **kwargs):
        cartesian = kwargs['container']
        data_generator = kwargs['data_generator']
        self.generate_nodes(cartesian, data_generator)

    @staticmethod
    def container_class():
        return alvi.client.containers.Cartesian


if __name__ == "__main__":
    GrahamConvexHull.start()