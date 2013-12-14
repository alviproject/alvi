from alvi.client.scenes.base import Scene
from alvi.client.containers.tree import Tree


class TreeCreateNode(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def run(self, tree):
        node = tree.create_root(value=0)
        self.nodes.append(node)
        node = self.nodes[0].create_child(value=1)
        self.nodes.append(node)
        node = self.nodes[0].create_child(value=2)
        self.nodes.append(node)
        node = self.nodes[1].create_child(value=3)
        self.nodes.append(node)
        node = self.nodes[1].create_child(value=4)
        self.nodes.append(node)
        node = self.nodes[4].create_child(value=5)
        self.nodes.append(node)
        node = self.nodes[4].create_child(value=6)
        self.nodes.append(node)
        tree.sync()

    @classmethod
    def container_class(cls):
        return Tree