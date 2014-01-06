import unittest
from alvi.client.data_generators.random import RandomDataGenerator


class TestRandom(unittest.TestCase):
    def test(self):
        generator = RandomDataGenerator(dict(n=8))
        self.assertEquals(len(list(generator.values)), 8)
