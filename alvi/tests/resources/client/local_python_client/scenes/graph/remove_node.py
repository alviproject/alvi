from . import create_node


class GraphRemoveNode(create_node.GraphCreateNode):
    def run(self, graph, options):
        super().run(graph, options)
        graph.remove_node(3)
        graph.sync()