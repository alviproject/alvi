import unittest
import alvi.client.scenes.red_black_tree
import logging
import random
from alvi.client.api import Pipe
from mock import MagicMock


class TestRedBlackTreeInsert(unittest.TestCase):
    def setUp(self):
        self.pipe = Pipe("test_scene")
        self.pipe.send = MagicMock()
        self.pipe.sync = MagicMock()
        container_class = alvi.client.scenes.red_black_tree.RedBlackTree.container_class()
        self.container = container_class(self.pipe)
        self.scene = alvi.client.scenes.red_black_tree.RedBlackTree()

    def test_ascending(self):
        self.scene.run_sequence(self.container, range(0, 20))

    def test_descending(self):
        self.scene.run_sequence(self.container, range(20, 0))

    def test_random(self):
        seq = [random.randint(0, 100) for i in range(100)]
        logging.debug('testing with random sequence: %s' % seq)
        self.scene.run_sequence(self.container, seq)


