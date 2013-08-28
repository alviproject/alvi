from playground.spaces import BinaryTree
import random
import time


class BinarySearchTree(object):
    def __init__(self, n):
        self.n = n
        self.Space = BinaryTree

    def run(self, space):
        self.space = space
        for i in xrange(self.n):
            x = random.randint(0, self.n)
            self.insert(x)
            time.sleep(1)

    def insert(self, value):
        node = self.space.root
        while True:
            if node.value > value:
                if node.left_child:
                    node = node.left_child
                    continue
                node.left_child = value
                return
            if node.right_child:
                node = node.right_child
                continue
            node.right_child = value
            return