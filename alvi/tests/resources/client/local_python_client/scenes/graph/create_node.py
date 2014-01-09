from alvi.client.scenes.base import Scene
from alvi.client.containers.graph import Graph


class GraphCreateNode(Scene):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def run(self, **kwargs):
        data_generator = kwargs['data_generator']
        graph = kwargs['container']
        value = next(data_generator.values)
        node = graph.create_node(value)
        self.nodes.append(node)
        for i, value in enumerate(data_generator.values):
            node = node.children.create(i+1)
            self.nodes.append(node)
        node.create_edge(self.nodes[0])
        graph.sync()

    @classmethod
    def container_class(cls):
        return Graph