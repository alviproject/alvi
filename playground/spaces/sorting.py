import cartesian
import time
from functools import total_ordering


class Item(cartesian.Point):
    """
    @total_ordering cannot be used because it would cause errors in number of comparisons
     (fe. __gt__ calls __le__ and __eq__, which means that one __gt__ call would increments number of comparisons twice
       first for __le__ and secondly for __eq__)
    """
    def __init__(self, space, value):
        cartesian.Point.__init__(self, value)
        self.space = space
        self.space.stats.assignments = 0
        self.space.stats.comparisons = 0

    @property
    def value(self):
        return self.x

    @value.setter
    def value(self, v):
        self.x = v
        self.space.stats.assignments += 1

    def __lt__(self, other):
        self.space.stats.comparisons += 1
        return self.x < other.x

    def __le__(self, other):
        self.space.stats.comparisons += 1
        return self.x <= other.x

    def __gt__(self, other):
        self.space.stats.comparisons += 1
        return self.x > other.x

    def __ge__(self, other):
        self.space.stats.comparisons += 1
        return self.x >= other.x

    def __eq__(self, other):
        self.space.stats.comparisons += 1
        return self.x == other.x


class Sorting(cartesian.Cartesian):
    def create_item(self, value):
        item = Item(self, value)
        self.add_point(item)
        return item

    @property
    def items(self):
        return self.points

    def swap(self, item_a, item_b):
        tmp = item_a.value
        item_a.value = item_b.value
        item_b.value = tmp
        self.update_point(item_a)
        self.update_point(item_b)
        time.sleep(1)