from . import create_node


class GraphUpdateNode(create_node.GraphCreateNode):
    def run(self, graph, options):
        super().run(graph, options)
        self.nodes[3].update(10)
        graph.sync()