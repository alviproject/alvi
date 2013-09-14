import unittest
from playground.scenes import Pipe
from queue import Queue


class TestContainer(unittest.TestCase):
    def setUp(self):
        queue = Queue()  # production code uses multiprocessing.Queue, but for testing this one will suit
        self.pipe = Pipe(queue)