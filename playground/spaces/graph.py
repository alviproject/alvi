from . import base


class Graph(base.Space):
    template = "spaces/graph.html"

    def create_node(self, id, value, parent_id):
        return ('create_node', dict(
            id=id,
            value=value,
            parent_id=parent_id,
        ))

    def create_edge(self, node1_id, node2_id):
        return ('create_edge', dict(
            node1_id=node1_id,
            node2_id=node2_id,
        ))
