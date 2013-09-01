from .space import Space
from .space import Node


class TreeNode(object):
    def __init__(self, space, parent, value):
        self._node = Node(space)
        self.value = value
        self.parent = parent
        self.children = []
        space.stats.nodes += 1
        space._space.add_node(self)
        parent_id = parent.id if parent else 0
        #TODO action type shall be on different level than action parameters, it will make JS mapping easier
        space.pipe.put(dict(
            type='create_node',
            id=self.id,
            parent_id=parent_id,
            value=self.value,
        ))

    @property
    def id(self):
        return self._node.id

    @property
    def space(self):
        return self._node.space

    def create_child(self, value):
        child = TreeNode(self.space, self, value)
        self.children.append(child)


class Tree(object):
    template = "spaces/tree.html"

    def __init__(self, pipe, RootNode=TreeNode):
        self._space = Space(pipe)
        self.stats.nodes = 0
        self.root = RootNode(self, None, 0)

    @property
    def nodes(self):
        return self._space.nodes

    @property
    def stats(self):
        return self._space.stats

    @property
    def pipe(self):
        return self._space.pipe

    def next_node_id(self):
        return self._space.next_node_id()