class Stats(object):
    def __init__(self, queue):
        object.__setattr__(self, 'queue', queue)

    def __setattr__(self, name, value):
        self.queue.put(dict(
            type='update_stats',
            name=name,
            value=value,
        ))
        return object.__setattr__(self, name, value)


class Node(object):
    def __init__(self, space):
        self.id = space.next_node_id()
        self.space = space


class Space(object):
    """abstract space, not to be used directly"""

    def __init__(self, queue):
        self.queue = queue
        self.stats = Stats(queue)
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def next_node_id(self):
        return len(self.nodes)

