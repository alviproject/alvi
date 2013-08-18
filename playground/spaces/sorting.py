import cartesian
import time


class Item(object):
    """
    @total_ordering cannot be used because it would cause errors in number of comparisons
     (fe. __gt__ calls __le__ and __eq__, which means that one __gt__ call would increments number of comparisons twice
       first for __le__ and secondly for __eq__)
    """
    def __init__(self, space, value):
        self._point = cartesian.Point(space, value, space.next_node_id()+1)
        self.space.stats.assignments = 0
        self.space.stats.comparisons = 0

    @property
    def space(self):
        return self._point.space

    @property
    def value(self):
        return self._point.x

    @value.setter
    def value(self, v):
        self._point.x = v
        self.space.stats.assignments += 1

    def __lt__(self, other):
        self.space.stats.comparisons += 1
        return self.value < other.value

    def __le__(self, other):
        self.space.stats.comparisons += 1
        return self.value <= other.value

    def __gt__(self, other):
        self.space.stats.comparisons += 1
        return self.value > other.value

    def __ge__(self, other):
        self.space.stats.comparisons += 1
        return self.value >= other.value

    def __eq__(self, other):
        self.space.stats.comparisons += 1
        return self.value == other.value


class Sorting(object):
    template = cartesian.Cartesian.template

    def __init__(self, queue):
        self._cartesian = cartesian.Cartesian(queue)

    @property
    def items(self):
        return self._cartesian.points

    @property
    def queue(self):
        return self._cartesian.queue

    @property
    def stats(self):
        return self._cartesian.stats

    def next_node_id(self):
        return self._cartesian.next_node_id()

    def create_item(self, value):
        item = Item(self, value)
        self._cartesian.add_point(item)
        return item

    def swap(self, item_a, item_b):
        tmp = item_a.value
        item_a.value = item_b.value
        item_b.value = tmp
        time.sleep(1)