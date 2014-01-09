from alvi.client.containers import Array
from alvi.client.scenes.base import Scene


class ArrayCreateNode(Scene):
    def run(self, **kwargs):
        data_generator = kwargs['data_generator']
        array = kwargs['container']
        array.init(data_generator.quantity())
        for i, value in enumerate(data_generator.values):
            array[i] = value
        array.sync()

    @classmethod
    def container_class(cls):
        return Array