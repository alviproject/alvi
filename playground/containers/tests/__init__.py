import unittest
from playground.scenes import Pipe
from multiprocessing import Queue


class TestContainer(unittest.TestCase):
    def setUp(self):
        queue = Queue()
        self.pipe = Pipe(queue)