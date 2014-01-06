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
        #a node does not always have a parent e.g: attaching node that was formerly root
        if child.parent:
            child.parent.children._children.remove(child)
        alvi.client.api.tree.insert_child(self._node._container._pipe, self._node.id, index, child.id)
        self._children.insert(index, child)
        child.parent = self._node

    def __getitem__(self, index):
        return self._children[index]

    def __len__(self):
        return len(self._children)


class Node(base.Node):
    def __init__(self, container, parent, data):
        super().__init__(container, parent, data)
        self.children = Children(self)
        self.parent = parent

    def __repr__(self):
        return self._value.__repr__()


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
