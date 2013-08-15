from playground.spaces import Sorting
import random


class Booble(object):
    def __init__(self, n):
        self.n = n
        self.Space = Sorting

    def run(self, space):
        for i in xrange(self.n):
            space.create_item(random.randint(1, self.n))

        changed = True
        while changed:
            changed = False
            for j in xrange(1, len(space.items)):
                item_a = space.items[j]
                item_b = space.items[j - 1]
                if item_a > item_b:
                    space.swap(item_a, item_b)
                    changed = True