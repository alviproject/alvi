import random

from . import base
import alvi.client.containers


class CreateTree(base.Scene):
    def run(self, **kwargs):
        tree = kwargs['container']
        data_generator = kwargs['data_generator']
        nodes = []
        value = next(data_generator.values)
        node = tree.create_root(value)
        nodes.append(node)
        tree.sync()
        for i, value in enumerate(data_generator.values):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.children.create(value)
            nodes.append(node)
            tree.sync()

    @staticmethod
    def container_class():
        return alvi.client.containers.Tree


if __name__ == "__main__":
    CreateTree.start()