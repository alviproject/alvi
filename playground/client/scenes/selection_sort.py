from playground.client.scenes.sort import Sort


class SelectionSort(Sort):
    def sort(self, array):
        min_marker = array.create_marker("min", 0)
        current_marker = array.create_marker("current", 0)
        for current in range(0, self.n):
            min = current
            for j in range(current, self.n):
                array.stats.comparisons += 1
                if array[j] < array[min]:
                    min = j
            current_marker.move(current)
            min_marker.move(min)
            array.sync()
            self.swap(array, current, min)
            array.sync()