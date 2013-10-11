from . import create_node
import alvi.client.api.graph as graph


class GraphRemoveNode(create_node.GraphCreateNode):
    def run(self, pipe):
        super().run(pipe)
        graph.remove_node(pipe, 3)
        pipe.sync()