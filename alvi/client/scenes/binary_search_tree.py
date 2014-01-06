import random

from . import base
import alvi.containers


class BinarySearchTree(base.Scene):
    def run(self, **kwargs):
        data_generator = kwargs['data_generator']
        tree = kwargs['container']

        #create root
        tree.create_root(next(data_generator.values))
        tree.sync()

        #create all other elements
        for value in data_generator.values:
            self.insert(tree, value)
            tree.sync()

    @staticmethod
    def insert(tree, value):
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