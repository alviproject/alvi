from playground.spaces import Tree
import random
import time


class CreateTree(object):
    Space = Tree

    def __init__(self, n):
        self.n = n

    def run(self, space):
        for i in range(self.n):
            x = random.randint(0, i)
            parent = space.nodes[x]
            parent.create_child(i + 1)