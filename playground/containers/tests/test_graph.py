from playground.containers import Graph
from playground.containers.tests import TestContainer


class TestGraph(TestContainer):
    def test_create(self):
        graph = Graph(self.pipe)
        node = graph.create_node(10)
        assert node.value == 10
