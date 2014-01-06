from alvi.client.data_generators.random import RandomDataGenerator
from alvi.client.data_generators.sequenced import SequencedDataGenerator

generators = dict(
    random=RandomDataGenerator,
    sequenced=SequencedDataGenerator,
)


def make_data_generator(options):
    generator_class = generators[options['generator']]
    return generator_class(options)