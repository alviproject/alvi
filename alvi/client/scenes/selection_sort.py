from alvi.client.scenes.sort import Sort


class SelectionSort(Sort):
    def sort(self, **kwargs):
        array = kwargs['container']
        data_generator = kwargs['data_generator']
        min_marker = array.create_marker("min", 0)
        current_marker = array.create_marker("current", 0)
        for current in range(0, data_generator.quantity()):
            min = current
            for j in range(current, data_generator.quantity()):
                array.stats.comparisons += 1
                if array[j] < array[min]:
                    min = j
            current_marker.move(current)
            min_marker.move(min)
            array.sync()
            self.swap(array, current, min)
            array.sync()