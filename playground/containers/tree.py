from . import base
from .base import action
import playground.spaces.tree


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._node = playground.spaces.tree.TreeNode(container._space, parent, value)

    @property
    def value(self):
        return self._node.value

    def create_child(self, value):
        return Node(self._container, self, value)


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

    @action
    def create_node(self, id, value, parent_id):
        return self._space.create_node(id, value, parent_id)

    @action
    def update_node(self, id, value):
        return self._space.update_node(id, value)