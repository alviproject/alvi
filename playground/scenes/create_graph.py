import random


class CreateGraph(object):
    def __init__(self, n):
        self.n = n

    def run(self, graph):
        nodes = []
        node = graph.create_node(random.randint(0, self.n))
        nodes.append(node)
        for i in range(self.n-1):
            x = random.randint(0, i)
            parent = nodes[x]
            node = parent.create_child(i)
            nodes.append(node)