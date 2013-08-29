from . import tree


class BinaryTreeNode(object):
    LEFT_CHILD_INDEX = 0
    RIGHT_CHILD_INDEX = 1

    def __init__(self, space, parent, value):
        self._treeNode = tree.TreeNode(space, parent, value)
        self._treeNode.children = [None, None]  # left and right child

    @property
    def id(self):
        return self._treeNode.id

    @property
    def space(self):
        return self._treeNode.space

    @property
    def value(self):
        return self._treeNode.value

    @property
    def left_child(self):
        return self._treeNode.children[BinaryTreeNode.LEFT_CHILD_INDEX]

    @property
    def right_child(self):
        return self._treeNode.children[BinaryTreeNode.RIGHT_CHILD_INDEX]

    @left_child.setter
    def left_child(self, value):
        self._treeNode.children[BinaryTreeNode.LEFT_CHILD_INDEX] = BinaryTreeNode(self.space, self, value)

    @right_child.setter
    def right_child(self, value):
        self._treeNode.children[BinaryTreeNode.RIGHT_CHILD_INDEX] = BinaryTreeNode(self.space, self, value)


class BinaryTree(object):
    template = tree.Tree.template

    def __init__(self, queue):
        self._tree = tree.Tree(queue, BinaryTreeNode)

    @property
    def nodes(self):
        return self._tree.nodes

    @property
    def stats(self):
        return self._tree.stats

    @property
    def queue(self):
        return self._tree.queue

    def next_node_id(self):
        return self._tree.next_node_id()

    @property
    def root(self):
        return self._tree.root

    @property
    def _space(self):
        return self._tree._space
