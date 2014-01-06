import abc

from . import base
import alvi.client.containers


class Sort(base.Scene):
    """abstract scene, not to be used directly"""
    def swap(self, array, index_a, index_b):
        t = array[index_a]
        array[index_a] = array[index_b]
        array[index_b] = t
        array.stats.assignments += 2

    def init(self, array, n):
        array.stats.comparisons = 0
        array.stats.assignments = 0
        array.init(n)
        array.sync()

    def generate_points(self, array, data_generator):
        for i, value in enumerate(data_generator.values):
            array[i] = value
        array.sync()

    @abc.abstractmethod
    def sort(self, **kwargs):
        raise NotImplementedError

    def run(self, **kwargs):
        data_generator = kwargs['data_generator']
        array = kwargs['container']
        array.stats.elements = data_generator.quantity()
        self.init(array, data_generator.quantity())
        self.generate_points(array, data_generator)
        self.sort(**kwargs)

    @staticmethod
    def container_class():
        return alvi.client.containers.Array

    def test(self, array, test_case):
        for i in range(1, array.size()):
            previous = array[i-1]
            current = array[i]
            test_case.assertLessEqual(previous, current)