from alvi.client.containers import tree
from . import base
import logging
import random
import alvi.client.api.tree

log = logging.getLogger(__package__)


class Colors:
    class _color:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return '{0}'.format(self.name)
    BLACK = _color('black')
    RED = _color('red')


class RedBlackNode:
    def __init__(self, container, parent, value, color):
        if parent is not None:
            self._node = parent._node.children.create(value)
        else:
            self._node = tree.Node(container, None, value)
        self.parent = parent
        self._color = None
        self.color = color
        if value is not None:
            self.init_nil_nodes()

    def init_nil_nodes(self):
        self.create_left_child(None, Colors.BLACK)
        self.create_right_child(None, Colors.BLACK)

    def create_left_child(self, value, color):
        return self._create_child('left', value, color)

    def _create_child(self, index, value, color):
        try:
            children = self._children
        except AttributeError:
            children = self._create_children()

        created = children[index]
        if created.value is None and value is not None:  # we are substituting nilnode for non-nil node
            created.init_nil_nodes()
        created.value = value
        created.color = color
        return children[index]

    def _create_children(self):
        left = RedBlackNode(self._container, self, None, Colors.BLACK)
        right = RedBlackNode(self._container, self, None, Colors.BLACK)
        self._children = {'left': left, 'right': right}
        return self._children

    def create_right_child(self, value, color):
        return self._create_child('right', value, color)

    def _child(self, index):
        try:
            child = self._children[index]
        except AttributeError:
            return None
        return child

    def is_left_child(self):
        if self.parent:
            return self.parent.left_child is self

    def is_right_child(self):
        if self.parent:
            return self.parent.right_child is self

    @property
    def left_child(self):
        return self._child('left')

    @left_child.setter
    def left_child(self, node):
        self._node.children.insert(0, node._node)
        if node.parent:
            if 'left' in node.parent._children and node.parent._children['left'] == node:
                del node.parent._children['left']
            if 'right' in node.parent._children and  node.parent._children['right'] == node:
                del node.parent._children['right']
        if 'left' in self._children:
            orphaned_node = self._children['left']
            orphaned_node.parent = None
        self._children['left'] = node
        node.parent = self

    @property
    def right_child(self):
        return self._child('right')

    @right_child.setter
    def right_child(self, node):
        self._node.children.append(node._node)
        if node.parent:
            if 'left' in node.parent._children and node.parent._children['left'] == node:
                del node.parent._children['left']
            if 'right' in node.parent._children and  node.parent._children['right'] == node:
                del node.parent._children['right']
        if 'right' in self._children:
            orphaned_node = self._children['right']
            orphaned_node.parent = None
        self._children['right'] = node
        node.parent = self

    def is_not_nilnode(self):
        return self.value is not None

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

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        previous_color = self._color
        if value == Colors.BLACK:
            if previous_color == Colors.RED:
                self._container.red_nodes.remove(self._node)
            self._container.black_nodes.append(self._node)
        if value == Colors.RED:
            if previous_color == Colors.BLACK:
                self._container.black_nodes.remove(self._node)
            self._container.red_nodes.append(self._node)
        self._color = value


class RedBlackTreeContainer:
    def __init__(self, *args, **kwargs):
        self._tree = tree.Tree(*args, **kwargs)
        self.red_nodes = self._tree.create_multi_marker('red nodes', color='red')
        self.black_nodes = self._tree.create_multi_marker('black nodes', color='grey')
        self.color_nodes = {Colors.RED: self.red_nodes, Colors.BLACK: self.black_nodes}

    @property
    def root(self):
        try:
            return self._root
        except AttributeError:
            return None

    def _create_root(self, value):
        if self.root:
            raise RuntimeError("Cannot set root more that once")
        self._root = RedBlackNode(self, None, value, Colors.BLACK)
        return self._root

    def change_root(self, new_root):
        n = new_root._node
        n.parent.children._children.remove(n)
        n.parent = None
        self._root = new_root
        self._tree._root = n
        alvi.client.api.tree.change_root(self._tree._pipe, n.id)


    @property
    def _pipe(self):
        return self._tree._pipe

    def sync(self):
        self._tree.sync()

    @classmethod
    def name(cls):
        return tree.Tree.__name__

    def insert(self, value):
        if self.root is None:
            self._create_root(value)
            node_inserted = self.root
        else:
            node = self.root
            while True:
                if node.value > value:
                    if node.left_child.is_not_nilnode():
                        node = node.left_child
                        continue
                    node_inserted = node.create_left_child(value, Colors.RED)
                    break
                if node.right_child.is_not_nilnode():
                    node = node.right_child
                    continue
                node_inserted = node.create_right_child(value, Colors.RED)
                break
        self._fix_rb_insert(node_inserted)

    def _fix_rb_insert(self, z):
        while z is not self.root and z.parent.color == Colors.RED:
            if z.parent.is_left_child():
                y = z.parent.parent.right_child
                if y.color == Colors.RED:
                    z.parent.color = Colors.BLACK
                    y.color = Colors.BLACK
                    z.parent.parent.color = Colors.RED
                    z = z.parent.parent
                else:
                    if z.is_right_child():
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = Colors.BLACK
                    z.parent.parent.color = Colors.RED
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left_child
                if y.color == Colors.RED:
                    z.parent.color = Colors.BLACK
                    y.color = Colors.BLACK
                    z.parent.parent.color = Colors.RED
                    z = z.parent.parent
                else:
                    if z.is_left_child():
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = Colors.BLACK
                    z.parent.parent.color = Colors.RED
                    self._left_rotate(z.parent.parent)
        self.root.color = Colors.BLACK

    def _left_rotate(self, x):
        y = x.right_child
        x.right_child = y.left_child
        if x == self.root:
            self.change_root(y)
        elif x.is_left_child():
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.left_child = x

    def _right_rotate(self, x):
        y = x.left_child
        x.left_child = y.right_child
        if x == self.root:
            self.change_root(y)
        elif x.is_left_child():
            x.parent.left_child = y
        else:
            x.parent.right_child = y
        y.right_child = x


class RedBlackTree(base.Scene):
    #more complete test cases in test/test_red_black_tree.py
    def test(self, tree, test_case):
        pass

    def run(self, **kwargs):
        _tree = kwargs['container']
        data_generator = kwargs['data_generator']
        self.run_sequence(_tree, data_generator.values)

    def run_sequence(self, tree, sequence):
        for node_value in sequence:
            tree.insert(node_value)
            tree.sync()

    @staticmethod
    def container_class():
        return RedBlackTreeContainer

if __name__ == "__main__":
    RedBlackTreeContainer.start()