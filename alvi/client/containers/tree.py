from . import base
import alvi.client.api.tree


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        self.children = []
        self.parent = parent

    def create_child(self, value):
        node = Node(self._container, self, value)
        self.children.append(node)
        return node

    def change_parent(self, new_parent):
        self.parent.children.remove(self)
        alvi.client.api.tree.change_parent(self._container._pipe, self.id, new_parent.id)
        new_parent.children.append(self)
        self.parent = new_parent


class Tree(base.Container):
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