from . import base
import playground.spaces.tree


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._node = playground.spaces.tree.TreeNode(container._space, parent, value)

    @property
    def value(self):
        return self._point.x

    def create_child(self, value):
        return Node(self._container, self, value)


class Tree(base.Container):
    #TODO
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