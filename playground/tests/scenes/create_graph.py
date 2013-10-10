"""various graph operations"""

import playground.client.api
import playground.client.api.graph as graph
import playground.client.containers


class CreateGraph(playground.client.api.BaseScene):
    def run(self, pipe):
        n = 4
        graph.create_node(pipe, id=0, parent_id=0, value=0)
        for i in range(n-1):
            graph.create_node(pipe, id=i+1, parent_id=i, value=i+1)
        graph.create_edge(pipe, node1_id=0, node2_id=n-1)
        pipe.sync()

    @classmethod
    def container_name(cls):
        return "Graph"


if __name__ == "__main__":
    CreateGraph.start()