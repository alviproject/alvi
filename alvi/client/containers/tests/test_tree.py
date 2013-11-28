import unittest
from unittest.mock import MagicMock, PropertyMock
from unittest.mock import patch
from unittest.mock import call
from alvi.client.containers.tree import Tree
from alvi.client.api import Pipe


_cache = dict()


def generate_id(obj):
    return _cache.setdefault(id(obj), len(_cache))


@patch('alvi.client.containers.base.generate_id', MagicMock(side_effect=generate_id))
class TestTree(unittest.TestCase):
    def setUp(self):
        _cache.clear()
        self.pipe = Pipe("test_scene")
        self.pipe.send = MagicMock()

    def create_sample_tree(self):
        tree = Tree(self.pipe)
        root = tree.create_root(0)
        node1 = root.create_child(1)
        root.create_child(2)
        node1.create_child(3)
        node4 = node1.create_child(4)
        node4.create_child(5)
        node4.create_child(6)
        return tree

    def test_create_root(self):
        tree = Tree(self.pipe)
        root = tree.create_root(0)
        self.assertEquals(tree.root, root)
        self.assertEquals(root.value, 0)
        self.assertRaises(RuntimeError, tree.create_root, 0)

    def test_create_tree(self):
        tree = self.create_sample_tree()
        self.assertEquals(len(tree.root.children), 2)
        node1 = tree.root.children[0]
        self.assertEquals(len(node1.children), 2)
        self.assertEquals(node1.value, 1)
        self.assertEquals(len(tree.root.children[1].children), 0)
        expected_calls = [
            call('create_node', (0,), {'parent_id': 0, 'value': 0, 'id': 0}),
            call('create_node', (1,), {'parent_id': 0, 'value': 1, 'id': 1}),
            call('create_node', (2,), {'parent_id': 0, 'value': 2, 'id': 2}),
            call('create_node', (3,), {'parent_id': 1, 'value': 3, 'id': 3}),
            call('create_node', (4,), {'parent_id': 1, 'value': 4, 'id': 4}),
            call('create_node', (5,), {'parent_id': 4, 'value': 5, 'id': 5}),
            call('create_node', (6,), {'parent_id': 4, 'value': 6, 'id': 6})
        ]
        self.pipe.send.assert_has_calls(expected_calls)

    def test_change_parent(self):
        tree = self.create_sample_tree()
        node1 = tree.root.children[0]
        self.assertEquals(len(node1.children), 2)
        node2 = tree.root.children[1]
        node4 = tree.root.children[0].children[1]
        self.assertEquals(node4.value, 4)
        self.assertEquals(node4.id, 4)
        self.assertEquals(node4.parent, node1)

        node4.change_parent(node2)
        self.pipe.send.assert_called_with('change_parent', (4,), {'parent_id': 2, 'id': 4})

        self.assertEquals(node4.parent, node2)
        self.assertEquals(len(node1.children), 1)
        self.assertEquals(len(node2.children), 1)