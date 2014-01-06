import random
from alvi.client.data_generators.base import DataGenerator


class RandomDataGenerator(DataGenerator):
    def _values(self):
        qty = self.quantity()
        return (random.randint(1, qty) for _ in range(qty)).__iter__()