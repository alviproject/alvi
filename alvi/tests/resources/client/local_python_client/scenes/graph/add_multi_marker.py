from . import create_node


class GraphAddMultiMarker(create_node.GraphCreateNode):
    def run(self, **kwargs):
        super().run(**kwargs)
        graph = kwargs['container']
        multi_marker = graph.create_multi_marker("multi marker")
        multi_marker.append(self.nodes[1])
        multi_marker.append(self.nodes[2])
        graph.sync()