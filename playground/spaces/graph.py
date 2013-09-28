from . import space


class Node(object):
    def __init__(self, _space, parent, value):
        self._space = _space
        self._node = space.Node(self._space)
        self._value = value
        self.parent = parent
        self.children = []
        self._space.stats.nodes += 1
        self._space.add_node(self)
        parent_id = parent.id if parent else 0
        #TODO action type shall be on different level than action parameters, it will make JS mapping easier
        self.space.pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            parent_id=parent_id,
            value=self.value,
        ))
        self.space.sync(1)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self._space.pipe.send('set_node_value', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))
        self._space.sync(1)

    @property
    def id(self):
        return self._node.id

    @property
    def space(self):
        return self._node.space

    def create_child(self, value):
        child = TreeNode(self.space, self, value)
        self.children.append(child)


class Graph(object):
    template = "spaces/graph.html"

    def __init__(self):
        self._space = space.Space()

    @property
    def nodes(self):
        return self._space.nodes

    @property
    def stats(self):
        return self._space.stats

    @property
    def pipe(self):
        return self._space.pipe

    def add_node(self, node):
        return self._space.add_node(node)

    def sync(self, level):
        self._space.sync(level)

    def next_node_id(self):
        return self._space.next_node_id()

    def create_node(self, id, value, parent_id):
        return ('create_node', dict(
            id=id,
            value=value,
            parent_id=parent_id,
        ))
