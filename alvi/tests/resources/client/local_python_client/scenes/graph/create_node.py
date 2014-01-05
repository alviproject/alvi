from alvi.client.scenes.base import Scene
from alvi.client.containers.graph import Graph
from django import forms


class GraphCreateNode(Scene):
    class Form(Scene.Form):
        n = forms.IntegerField(initial=4)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def run(self, graph, options):
        n = int(options['n'])
        node = graph.create_node(0)
        self.nodes.append(node)
        for i in range(n-1):
            node = node.children.create(i+1)
            self.nodes.append(node)
        node.create_edge(self.nodes[0])
        graph.sync()

    @classmethod
    def container_class(cls):
        return Graph