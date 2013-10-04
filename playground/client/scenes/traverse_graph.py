import random

from . import base
import playground.client.containers


class TraverseGraph(base.Scene):
    """depth first graph traversing"""
    #TODO this class should inherit from CreateGraph as soon as synchronization management will be implemented
    def generate(self, graph):
        n = 64
        edge_factor = 3
        nodes = []
        first_node = graph.create_node(0)
        nodes.append(first_node)
        for i in range(n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i+1)
            nodes.append(node)
            if i % edge_factor == 0:
                x = random.randint(0, i)
                node1 = nodes[x]
                node.create_edge(node1)
        return first_node

    def traverse(self, marker, graph, node):
        if node in marker:
            return
        marker.add(node)
        graph.stats.traversed_nodes += 1
        graph.sync()
        for child in node.children():
            self.traverse(marker, graph, child)

    def run(self, graph):
        first_node = self.generate(graph)
        marker = graph.create_multi_marker("Traversed")
        graph.stats.traversed_nodes = 0
        self.traverse(marker, graph, first_node)

    @staticmethod
    def container_class():
        return playground.client.containers.Graph


if __name__ == "__main__":
    TraverseGraph.start()