from playground.scenes.sort import Sort
import random


class Booble(Sort):
    def sort(self, array):
        changed = True
        delta = 0
        right_marker = array.create_marker("right", array.size()-1)
        while changed:
            changed = False
            for j in range(1, array.size()-delta):
                item_a = array[j]
                item_b = array[j - 1]
                if item_a < item_b:
                    self.swap(array, j, j - 1)
                    changed = True
                    array.stats.assignments += 2
                array.stats.comparisons += 1
            delta += 1
            right_marker.move(array.size()-delta)
            array.sync()
