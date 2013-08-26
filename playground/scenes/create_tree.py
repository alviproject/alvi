from playground.spaces import Tree
import random
import time


class CreateTree(object):
    def __init__(self, n):
        self.n = n
        self.Space = Tree

    def run(self, space):
        for i in xrange(self.n):
            x = random.randint(0, i)
            parent = space.nodes[x]
            parent.create_child(i + 1)
            time.sleep(1)