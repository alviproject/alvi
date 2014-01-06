import random

from . import base
import alvi.client.containers


class CreateGraph(base.Scene):
    def run(self, **kwargs):
        graph = kwargs['container']
        data_generator = kwargs['data_generator']
        edge_factor = 3
        nodes = []
        value = next(data_generator.values)
        node = graph.create_node(value)
        graph.sync()
        nodes.append(node)
        for i, value in enumerate(data_generator.values):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.children.create(value)
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