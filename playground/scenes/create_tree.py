import random

from . import base
import playground.containers


class CreateTree(base.Scene):
    Container = playground.containers.Tree

    def run(self, tree, form_data):
        n = form_data['n']
        nodes = []
        node = tree.create_root(random.randint(0, n))
        nodes.append(node)
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i)
            nodes.append(node)