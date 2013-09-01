import time


class Stats(object):
    def __init__(self, pipe):
        object.__setattr__(self, 'pipe', pipe)

    def __setattr__(self, name, value):
        if False:  #TODO
            self.pipe.send(dict(
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

    def __init__(self, pipe):
        self.pipe = pipe
        self.stats = Stats(pipe)
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def next_node_id(self):
        return len(self.nodes)

    def sync(self, level):
        self.pipe.sync()
        time.sleep(1)

