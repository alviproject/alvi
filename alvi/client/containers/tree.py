from . import base
import alvi.client.api.tree


class Children:
    def __init__(self, node):
        self._children = []
        self._node = node

    def create(self, value):
        node = Node(self._node._container, self._node, value)
        self._children.append(node)
        return node

    def append(self, child):
        self.insert(len(self), child)

    def insert(self, index, child):
        child.parent.children.remove(child)
        alvi.client.api.tree.insert_child(self._node._container._pipe, self._node.id, index, child.id)
        self._children.insert(index, child)
        child.parent = self._node

    def remove(self, child):
        self._children.remove(child)

    def __getitem__(self, index):
        return self._children[index]

    def __len__(self):
        return len(self._children)


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        self.children = Children(self)
        self.parent = parent


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
        node.children._children.append(node)
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
