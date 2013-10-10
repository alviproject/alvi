from . import create_graph
import playground.client.api.graph as graph


class UpdateGraph(create_graph.CreateGraph):
    def run(self, pipe):
        super().run(pipe)
        graph.update_node(pipe, 3, 10)
        pipe.sync()
