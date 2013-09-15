from playground.scenes.sort import Sort


class SelectionSort(Sort):
    def sort(self, array):
        for i in range(0, self.n):
            min = i
            for j in range(i, self.n):
                array.stats.comparisons += 1
                if array[j] < array[min]:
                    min = j
            self.swap(array, i, min)
            array.sync()