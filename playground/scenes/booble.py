from playground.scenes.sort import Sort
import random


class Booble(Sort):
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