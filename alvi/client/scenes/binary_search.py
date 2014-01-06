import random

from . import base
import alvi.client.containers


class BinarySearch(base.Scene):
    def init(self, array, n):
        array.init(n)
        array.sync()

    def generate_points(self, array, data_generator):
        for i, value in enumerate(data_generator.values):
            array[i] = value
        array.sync()

    def search(self, array, value):
        left = 0
        right = array.size()-1
        left_marker = array.create_marker("left", left)
        right_marker = array.create_marker("right", right)
        array.sync()
        while left <= right:
            mid = (right + left) // 2
            if array[mid] > value:
                right = mid - 1
                if right >= 0:
                    right_marker.move(right)
            elif array[mid] < value:
                left = mid + 1
                if left < array.size():
                    left_marker.move(left)
            else:
                array.stats.found_id = mid
                array.create_marker("found", mid)
                array.sync()
                left_marker.remove()
                right_marker.remove()
                return
            array.sync()
        array.stats.not_found = ""

    def run(self, **kwargs):
        array = kwargs['container']
        data_generator = kwargs['data_generator']
        wanted_value = random.randint(1, data_generator.quantity())
        array.stats.wanted_value = wanted_value

        self.init(array, data_generator.quantity())
        self.generate_points(array, data_generator)

        for i, value in enumerate(sorted(array)):
            array[i] = value
        array.sync()
        self.search(array, wanted_value)
        array.sync()

    @staticmethod
    def container_class():
        return alvi.client.containers.Array


if __name__ == "__main__":
    BinarySearch.start()