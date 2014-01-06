import unittest
from alvi.client.data_generators.sequenced import SequencedDataGenerator


class TestSequenced(unittest.TestCase):
    def test_ascending(self):
        generator = SequencedDataGenerator(dict(n=8))
        self.assertEquals(next(generator.values), 0)
        self.assertEquals(list(generator.values), [1, 2, 3, 4, 5, 6, 7])

    def test_descending(self):
        generator = SequencedDataGenerator(dict(
            n=8,
            descending=True,
        ))
        self.assertEquals(list(generator.values), [7, 6, 5, 4, 3, 2, 1, 0])

    def test_quantity(self):
        generator = SequencedDataGenerator(dict(n=8))
        self.assertEquals(generator.quantity(), 8)