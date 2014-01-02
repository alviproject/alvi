import random

from . import base
import alvi.client.containers


class CreateGraph(base.Scene):
    def run(self, graph):
        n = 64
        edge_factor = 3
        nodes = []
        node = graph.create_node(0)
        graph.sync()
        nodes.append(node)
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.children.create(i+1)
            graph.sync()
            nodes.append(node)
            if i % edge_factor == 0:
                x = random.randint(0, i)
                node1 = nodes[x]
                node.create_edge(node1)
                graph.sync()
        graph.sync()
        return node

    @staticmethod
    def container_class():
        return alvi.client.containers.Graph


if __name__ == "__main__":
    CreateGraph.start()