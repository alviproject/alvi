from alvi.client.scenes.sort import Sort

#TODO: be able to visualize sequence of partition/quicksort calls
#TODO: markers

import logging
log = logging.getLogger(__name__)

class Quicksort(Sort):

    def __init__(self):
        self.qs_left = None
        self.qs_right = None
        self.part_partby = None
        self.part_i = None
        self.part_j = None

    def sort(self, **kwargs):
        array = kwargs['container']
        self.qs_left = array.create_marker('qs_left', 0)
        self.qs_right = array.create_marker('qs_right', 0)
        self.part_partby = array.create_marker('partition_by', 0)
        self.part_i = array.create_marker('partition_i', 0)
        self.part_j = array.create_marker('partition_j', 0)
        self._quicksort(array, 0, array.size()-1)
        array.sync()

    def _quicksort(self, A, p, r):
        log.info('quicksort p=%d, r=%d' % (p, r))
        self.qs_left.move(p)
        self.qs_right.move(r)
        if p < r:
            q = self._partition(A, p, r)
            log.info('q = %d'%q)
            self._quicksort(A, p, q-1)
            self._quicksort(A, q+1, r)

    def _partition(self, A, p, r):
        log.info('partition p=%d, r=%d' % (p, r))
        self.part_partby.move(r)
        x = A[r]
        i = p-1
        self.part_i.move(i)
        for j in range(p,r):
            self.part_j.move(j)
            A.sync()
            if A[j] < x:
                i += 1
                self.part_i.move(i)
                A[i], A[j] = A[j], A[i]
                A.sync()
        A[i+1], A[r] = A[r], A[i+1]
        self.part_partby.move(i+1)
        A.sync()
        return i+1

