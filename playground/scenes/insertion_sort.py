from playground.scenes.sort import Sort


class InsertionSort(Sort):
    def sort(self, array):
        right_marker = array.create_marker("right", 0)
        left_marker = array.create_marker("left", 0)
        left1_marker = array.create_marker("left+1", 0)
        array.sync()
        for right in range(0, self.n-1):
            right_marker.move(right+1)
            for i in range(0, right+1):
                left = right - i
                left_marker.move(left)
                left1_marker.move(left+1)
                array.sync()
                array.stats.comparisons += 1
                if array[left] > array[left+1]:
                    self.swap(array, left, left+1)
                    array.sync()
                else:
                    break
            array.sync()