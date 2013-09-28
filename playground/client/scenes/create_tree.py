import random

from . import base
import playground.client.containers


class CreateTree(base.Scene):
    def run(self, instance_id):
        n = 8
        tree = self.container_class()(instance_id)
        nodes = []
        node = tree.create_root(random.randint(0, n))
        nodes.append(node)
        tree.sync()
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i)
            nodes.append(node)
            tree.sync()

    @staticmethod
    def container_class():
        return playground.client.containers.Tree


if __name__ == "__main__":
    CreateTree.start()