import random

from . import base
import alvi.containers


class BinarySearchTree(base.Scene):
    def run(self, tree):
        n = 8
        x = random.randint(0, n)
        tree.create_root(x)
        tree.sync()
        for i in range(n-1):
            x = random.randint(0, n)
            self.insert(tree, x)
            tree.sync()

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

    @staticmethod
    def container_class():
        return alvi.client.containers.BinaryTree

if __name__ == "__main__":
    BinarySearchTree.start()