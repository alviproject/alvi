from playground.containers import BinaryTree
from playground.containers.tests import TestContainer


class TestBinaryTree(TestContainer):
    def test_create(self):
        tree = BinaryTree(self.pipe)
        root = tree.create_root(10)
        assert root.value == 10
        self.assertRaises(RuntimeError, tree.create_root, 12)

    def test_create_childs(self):
        tree = BinaryTree(self.pipe)
        root = tree.create_root(10)

        assert root.left_child is None
        assert root.right_child is None

        left_child = root.create_left_child(11)
        assert left_child.value == 11
        assert root.left_child == left_child
        assert root.right_child is None

        right_child = root.create_right_child(12)
        assert right_child.value == 12
        assert root.right_child == right_child

    def test_assign_value(self):
        tree = BinaryTree(self.pipe)
        root = tree.create_root(10)

        left_child = root.create_left_child(11)
        assert left_child.value == 11
        left_child.value = 12
        assert root.left_child.value == 12
