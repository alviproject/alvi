from playground.spaces import Sorting
import random


class Booble(object):
    Space = Sorting

    def __init__(self, n):
        self.n = n

    def swap(self, array, index_a, index_b):
        t = array[index_a]
        array[index_a] = array[index_b]
        array[index_b] = t

    def run(self, array):
        array.stats.comparisons = 0
        array.stats.assignments = 0
        array.init(self.n)

        for i in range(self.n):
            array[i] = random.randint(1, self.n)
        array.sync()

        changed = True
        while changed:
            changed = False
            for j in range(1, array.size()):
                item_a = array[j]
                item_b = array[j - 1]
                if item_a > item_b:
                    self.swap(array, j, j - 1)
                    changed = True
                    array.stats.assignments += 2
                array.stats.comparisons += 1
            array.sync()
