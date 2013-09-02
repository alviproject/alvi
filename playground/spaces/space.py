import time


class Stats(object):
    def __init__(self, pipe):
        object.__setattr__(self, 'pipe', pipe)

    def __setattr__(self, name, value):
        self.pipe.send("update_stats", (name, ), dict(
            name=name,
            value=value
        ))
        return object.__setattr__(self, name, value)


class Node(object):
    def __init__(self, space):
        self.id = space.next_node_id()
        self.space = space


class Space(object):
    """abstract space, not to be used directly"""

    def __init__(self, pipe):
        self.pipe = pipe #TODO pipe shall be private
        self.stats = Stats(pipe)
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def next_node_id(self):
        return len(self.nodes)

    def sync(self, level):
        self.pipe.sync()
        time.sleep(1)

