from . import base
import alvi.client.api.tree


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        #TODO create a proxy class that narrows children interface
        self.children = []
        self.parent = parent

    def create_child(self, value):
        node = Node(self._container, self, value)
        self.children.append(node)
        return node

    def append(self, child):
        self.insert(len(self.children), child)

    def insert(self, index, child):
        child.parent.children.remove(child)
        alvi.client.api.tree.insert_child(self._container._pipe, self.id, index, child.id)
        self.children.insert(index, child)
        child.parent = self


class Tree(base.Container):
    @property
    def root(self):
        try:
            return self._root
        except AttributeError:
            return None

    @root.setter
    def root(self, node):
        parent = node.parent
        node.parent.children.remove(node)
        node.children.append(node)
        parent.parent = node
        #TODO remove inconsistency - root node has parent set to None in containers and to self in low level API
        node.parent = None
        self._root = node
        alvi.client.api.tree.change_root(self._pipe, node.id)

    def create_root(self, value):
        if self.root:
            raise RuntimeError("Cannot set root more that once")
        self._root = Node(self, None, value)
        return self._root
