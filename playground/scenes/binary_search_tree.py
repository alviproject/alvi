import random


class BinarySearchTree(object):
    def __init__(self, n):
        self.n = n

    def run(self, tree):
        x = random.randint(0, self.n)
        tree.create_root(x)
        for i in range(self.n-1):
            x = random.randint(0, self.n)
            self.insert(tree, x)

    def insert(self, tree, value):
        node = tree.root
        while True:
            if node.value > value:
                if node.left_child:
                    node = node.left_child
                    continue
                return node.create_left_child(value)
            if node.right_child:
                node = node.right_child
                continue
            return node.create_right_child(value)
