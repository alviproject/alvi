import random

from . import base
import playground.containers


class BinarySearchTree(base.Scene):
    Container = playground.containers.BinaryTree

    def run(self, tree, form_data):
        n = form_data['n']
        x = random.randint(0, n)
        tree.create_root(x)
        for i in range(n-1):
            x = random.randint(0, n)
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
