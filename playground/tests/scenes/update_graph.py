from . import create_graph
import playground.client.api.internal.node as node


class UpdateGraph(create_graph.CreateGraph):
    def run(self, pipe):
        super().run(pipe)
        node.update(pipe, 3, 10)
        pipe.sync()
