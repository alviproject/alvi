from alvi.client.scenes import Scene
from alvi.client.containers.graph import Graph


class GraphCreateNode(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def run(self, graph):
        n = 4
        node = graph.create_node(0)
        self.nodes.append(node)
        for i in range(n-1):
            node = node.create_child(i+1)
            self.nodes.append(node)
        node.create_edge(self.nodes[0])
        graph.sync()

    @classmethod
    def container_class(cls):
        return Graph