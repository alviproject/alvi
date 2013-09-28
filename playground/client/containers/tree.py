from . import base


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        self.children = []

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