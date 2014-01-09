from alvi.tests.resources.client.local_python_client.scenes.graph.create_node import GraphCreateNode


class GraphMarker(GraphCreateNode):
    def run(self, **kwargs):
        super().run(**kwargs)
        graph = kwargs['container']

        marker0 = graph.create_marker("marker 0", self.nodes[2])
        marker1 = graph.create_marker("marker 1", self.nodes[3])
        graph.sync()
        marker1.move(self.nodes[1])
        graph.sync()