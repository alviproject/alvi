from . import create_node
import alvi.client.api.graph as graph


class GraphUpdateNode(create_node.GraphCreateNode):
    def run(self, pipe):
        super().run(pipe)
        graph.update_node(pipe, 3, 10)
        pipe.sync()