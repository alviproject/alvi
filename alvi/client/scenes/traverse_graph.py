from alvi.client.scenes.create_graph import CreateGraph


class TraverseGraph(CreateGraph):
    """depth first graph traversing"""
    def traverse(self, marker, graph, node):
        if node in marker:
            return
        marker.append(node)
        graph.stats.traversed_nodes += 1
        graph.sync()
        for child in node.children:
            self.traverse(marker, graph, child)

    def run(self, graph):
        with graph.postpone_sync():
            first_node = super().run(graph)
        marker = graph.create_multi_marker("Traversed")
        graph.stats.traversed_nodes = 0
        self.traverse(marker, graph, first_node)


if __name__ == "__main__":
    TraverseGraph.start()