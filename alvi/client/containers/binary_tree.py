from . import tree


class Node:
    def __init__(self, container, parent, value=None):
        self._node = tree.Node(container, parent, value)

    @property
    def _container(self):
        return self._node._container

    @property
    def id(self):
        return self._node.id

    @property
    def value(self):
        return self._node.value

    @value.setter
    def value(self, value):
        self._node.value = value

    def _create_children(self):
        left = Node(self._container, self)
        right = Node(self._container, self)
        self._children = [left, right]
        return self._children

    def _create_child(self, index, value):
        try:
            children = self._children
        except AttributeError:
            children = self._create_children()
        children[index].value = value
        return children[index]

    def create_left_child(self, value):
        return self._create_child(0, value)

    def create_right_child(self, value):
        return self._create_child(1, value)

    def _child(self, index):
        try:
            child = self._children[index]
        except AttributeError:
            return None
        if child.value is None:
            return None
        return child

    @property
    def left_child(self):
        return self._child(0)

    @property
    def right_child(self):
        return self._child(1)


class BinaryTree:
    def __init__(self, *args, **kwargs):
        self._tree = tree.Tree(*args, **kwargs)

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

    @property
    def _pipe(self):
        return self._tree._pipe

    def sync(self):
        self._tree.sync()

    @classmethod
    def name(cls):
        return tree.Tree.__name__

