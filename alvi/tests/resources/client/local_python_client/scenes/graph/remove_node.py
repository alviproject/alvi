from . import create_node


class GraphRemoveNode(create_node.GraphCreateNode):
    def run(self, graph):
        super().run(graph)
        graph.remove_node(3)
        graph.sync()