import cartesian
import time
from functools import total_ordering


@total_ordering
class Item(cartesian.Point):
    @property
    def value(self):
        return self.x

    @value.setter
    def value(self, v):
        self.x = v

    def __lt__(self, other):
        return self.x < other.x

    def __eq__(self, other):
        return self.x == other.x


class Sorting(cartesian.Cartesian):
    def create_item(self, value):
        item = Item(value)
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