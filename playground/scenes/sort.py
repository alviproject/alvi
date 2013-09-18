import abc
import random

from . import base
import playground.containers



class Sort(base.Scene):
    """abstract scene, not to be used directly"""
    def __init__(self, n):
        self.n = n

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
        self.init(array)
        self.generate_points(array)
        self.sort(array)

    def container_class(self):
        return playground.containers.Array
