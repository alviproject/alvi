from . import base


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._value = value
        self.parent = parent
        self.children = []
        parent_id = parent.id if parent else 0
        self._container._pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            parent_id=parent_id,
            value=self.value,
        ))

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

    def create_child(self, value):
        node = Node(self._container, self, value)
        self.children.append(node)
        return node


class Tree(base.Container):
    @classmethod
    def implementations(cls):
        return (cls, )

    @classmethod
    def space_class(cls):
        return playground.spaces.tree.Tree

    @property
    def root(self):
        try:
            return self._root
        except AttributeError:
            return None

    def create_root(self, value):
        if self.root:
            raise RuntimeError("Cannot set root more that once")
        self._root = Node(self, None, value)
        return self._root