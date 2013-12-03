from . import create_node


class GraphUpdateNode(create_node.GraphCreateNode):
    def run(self, graph):
        super().run(graph)
        self.nodes[3].update(10)
        graph.sync()