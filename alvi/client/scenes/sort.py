import abc
import random

from . import base
import alvi.client.containers


class Sort(base.Scene):
    """abstract scene, not to be used directly"""
    def swap(self, array, index_a, index_b):
        t = array[index_a]
        array[index_a] = array[index_b]
        array[index_b] = t
        array.stats.assignments += 2

    def init(self, array):
        array.stats.comparisons = 0
        array.stats.assignments = 0
        array.init(self.n)
        array.sync()

    def generate_points(self, array):
        for i in range(self.n):
            array[i] = random.randint(1, self.n)
        array.sync()

    @abc.abstractmethod
    def sort(self, array):
        raise NotImplementedError

    def run(self, array):
        self.n = 8
        self.init(array)
        self.generate_points(array)
        self.sort(array)

    @staticmethod
    def container_class():
        return alvi.client.containers.Array

    def test(self, array, test_case):
        for i in range(1, array.size()):
            previous = array[i-1]
            current = array[i]
            test_case.assertLessEqual(previous, current)