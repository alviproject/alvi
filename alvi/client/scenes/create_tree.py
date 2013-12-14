import random

from . import base
import alvi.client.containers


class CreateTree(base.Scene):
    def run(self, tree):
        n = 8
        nodes = []
        node = tree.create_root(0)
        nodes.append(node)
        tree.sync()
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.children.create(i+1)
            nodes.append(node)
            tree.sync()

    @staticmethod
    def container_class():
        return alvi.client.containers.Tree


if __name__ == "__main__":
    CreateTree.start()