import random


class Booble(object):
    def __init__(self, n):
        self.n = n

    def swap(self, array, index_a, index_b):
        t = array[index_a]
        array[index_a] = array[index_b]
        array[index_b] = t

    def init(self, array):
        array.stats.comparisons = 0
        array.stats.assignments = 0
        array.init(self.n)
        array.sync()

    def generate_points(self, array):
        for i in range(self.n):
            array[i] = random.randint(1, self.n)
        array.sync()

    def sort(self, array):
        changed = True
        while changed:
            changed = False
            for j in range(1, array.size()):
                item_a = array[j]
                item_b = array[j - 1]
                if item_a < item_b:
                    self.swap(array, j, j - 1)
                    changed = True
                    array.stats.assignments += 2
                array.stats.comparisons += 1
            array.sync()

    def run(self, array):
        self.init(array)
        self.generate_points(array)
        self.sort(array)