from playground.spaces import Sorting
import random


class Booble(object):
    Space = Sorting

    def __init__(self, n):
        self.n = n

    def run(self, space):
        for i in range(self.n):
            space.create_item(random.randint(1, self.n))
        space.sync(1)

        changed = True
        while changed:
            changed = False
            for j in range(1, len(space.items)):
                item_a = space.items[j]
                item_b = space.items[j - 1]
                if item_a > item_b:
                    space.swap(item_a, item_b)
                    changed = True
            space.sync(1)
