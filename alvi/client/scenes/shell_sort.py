from alvi.client.scenes.sort import Sort


class ShellSort(Sort):
    def sort(self, **kwargs):
        array = kwargs['container']
        right_marker = array.create_marker("right", 0)
        left_marker = array.create_marker("left", 0)
        left_h_marker = array.create_marker("left+h", 0)
        array.sync()
        h = 1
        while h < array.size() // 3:
            h = 3 * h + 1
        while h >= 1:
            array.stats.h = h
            array.sync()
            right = 0
            while right < array.size()-h:
                right_marker.move(right+h)
                left = right
                while left >= 0:
                    left_marker.move(left)
                    left_h_marker.move(left+h)
                    #array.sync()
                    array.stats.comparisons += 1
                    if array[left] > array[left+h]:
                        self.swap(array, left, left+h)
                        #array.sync()
                    else:
                        break
                    left -= h
                right += h
                array.sync()
            h //= 3
        array.sync()
