import random


class BinarySearch(object):
    def __init__(self, n):
        self.n = n

    def init(self, array):
        array.init(self.n)
        array.sync()

    def generate_points(self, array):
        for i in range(self.n):
            array[i] = random.randint(1, self.n)
        array.sync()

    def search(self, array, value):
        left = 0
        right = len(array._nodes)-1 #TODO
        left_marker = array.create_marker("left", array._nodes[left]) #TODO
        right_marker = array.create_marker("right", array._nodes[right])
        array.sync()
        while left < right:
            mid = (right + left) // 2
            if array[mid] > value:
                right = mid - 1
                right_marker.move(array._nodes[right])
            elif array[mid] < value:
                left = mid + 1
                left_marker.move(array._nodes[left])
            else:
                array.stats.found_id = mid
                #TODO remove left and right marker, create found marker
                return
            array.sync()
        array.stats.not_found = ""

    def run(self, array):
        wanted_value = random.randint(0, self.n)
        array.stats.wanted_value = wanted_value

        self.init(array)
        self.generate_points(array)

        #TODO reconsider
        for i, value in enumerate(sorted(array)):
            array[i] = value
        array.sync()
        self.search(array, wanted_value)
        array.sync()