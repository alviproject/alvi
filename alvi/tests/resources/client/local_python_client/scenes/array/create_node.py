from alvi.client.containers import Array
from alvi.client.scenes.base import Scene


class ArrayCreateNode(Scene):
    def run(self, array):
        n = 4
        array.init(4)
        for i in range(n):
            array[i] = i
        array.sync()

    @classmethod
    def container_class(cls):
        return Array