from alvi.client.scenes.sort import Sort


class BoobleSort(Sort):
    def sort(self, array):
        changed = True
        right_marker = array.create_marker("right", array.size()-1)
        array.sync()
        right = array.size()
        while changed:
            changed = False
            for j in range(1, right):
                item_a = array[j]
                item_b = array[j - 1]
                if item_a < item_b:
                    self.swap(array, j, j - 1)
                    changed = True
                array.stats.comparisons += 1
            right -= 1
            right_marker.move(right)
            array.sync()
