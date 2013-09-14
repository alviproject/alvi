from playground.containers import Tree
from playground.containers.tests import TestContainer


class TestTree(TestContainer):
    def test_create(self):
        tree = Tree(self.pipe)
        root = tree.create_root(10)
        assert root.value == 10
        self.assertRaises(RuntimeError, tree.create_root, 12)

    def test_create_child(self):
        tree = Tree(self.pipe)
        root = tree.create_root(10)
        child = root.create_child(11)
        assert child.value == 11