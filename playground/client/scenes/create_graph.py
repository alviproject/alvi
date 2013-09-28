import random

from . import base
import playground.client.containers


class CreateGraph(base.Scene):
    def run(self, graph):
        n = 8
        nodes = []
        node = graph.create_node(random.randint(0, n))
        graph.sync()
        nodes.append(node)
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i)
            graph.sync()
            nodes.append(node)

    @staticmethod
    def container_class():
        return playground.client.containers.Graph


if __name__ == "__main__":
    CreateGraph.start()