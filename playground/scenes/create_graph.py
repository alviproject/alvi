import random

from . import base
import playground.containers


class CreateGraph(base.Scene):
    Container = playground.containers.Graph

    def run(self, graph, form_data):
        n = form_data['n']
        nodes = []
        node = graph.create_node(random.randint(0, n))
        nodes.append(node)
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i)
            nodes.append(node)
