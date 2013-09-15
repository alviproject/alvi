from . import base
import playground.spaces.tree


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._node = playground.spaces.tree.TreeNode(container._space, parent, value)

    @property
    def value(self):
        return self._node.value

    @value.setter
    def value(self, value):
        self._node.value = value

    def _create_children(self):
        left = Node(self._container, self, None)
        right = Node(self._container, self, None)
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


class BinaryTree(base.Container):
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