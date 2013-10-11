import random

from . import base
import alvi.client.containers


class BinarySearch(base.Scene):
    def init(self, array, n):
        array.init(n)
        array.sync()

    def generate_points(self, array, n):
        for i in range(n):
            array[i] = random.randint(1, n)
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
                right_marker.move(right)
            elif array[mid] < value:
                left = mid + 1
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

    def run(self, array):
        n = 8
        wanted_value = random.randint(1, n)
        array.stats.wanted_value = wanted_value

        self.init(array, n)
        self.generate_points(array, n)

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