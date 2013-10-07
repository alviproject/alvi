"""various graph operations"""

import playground.client.api
import playground.client.api.node as node
import playground.client.containers


class Graph(playground.client.api.BaseScene):
    def run(self, pipe):
        n = 4
        node.create(pipe, id=0, parent_id=0, value=0)
        for i in range(n-1):
            node.create(pipe, id=i+1, parent_id=i, value=i+1)
        node.create_edge(pipe, node1_id=0, node2_id=n-1)

        #node.update(pipe, 3, 10)

        pipe.sync()

    @classmethod
    def container_name(cls):
        return "Graph"


if __name__ == "__main__":
    Graph.start()