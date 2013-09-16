from playground.scenes.sort import Sort


class MergeSort(Sort):
    def merge(self, array, left, mid, right):
        temp = []
        for i in range(left, right):
            temp.append(array[i])
        i = 0
        j = right - mid
        k = 0
        while k < len(temp):
            if i >= mid - left:
                array[k+left] = temp[j]
                j += 1
            elif j >= len(temp):
                array[k+left] = temp[i]
                i += 1
            elif temp[i] < temp[j]:
                array[k+left] = temp[i]
                i += 1
            else:
                array[k+left] = temp[j]
                j += 1
            k += 1

    def _sort(self, array, left, right):
        if right - left <= 1:
            return
        mid = (left+right) // 2
        self._sort(array, left, mid)
        self._sort(array, mid, right)
        self.merge(array, left, mid, right)
        if (right-left) > self.n // 50:
            array.sync()

    def sort(self, array):
        self._sort(array, 0, self.n)
        array.sync()
#        mid = self.n // 2
#
#        temp = []
#        for i in range(mid):
#            temp.append(array[i])
#        temp.sort()
#        for i in range(mid):
#            array[i] = temp[i]
#
#        temp = []
#        for i in range(mid, self.n):
#            temp.append(array[i])
#        temp.sort()
#        for i in range(mid):
#            array[mid+i] = temp[i]
#
#        array.sync()
#        self.merge(array, 0, mid, self.n)
#        array.sync()
#