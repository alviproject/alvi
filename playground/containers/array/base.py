from .. import base


#TODO do we still need it?
#TODO iterators
class Array(base.Container):
    def init(self, size):
        if self._nodes:
            raise RuntimeError("Array was already initialized")
        for i in range(size):
            self._create_node()

    def __getitem__(self, key):
        return self._nodes[key].value

    def __setitem__(self, key, value):
        self._nodes[key].value = value

    def size(self):
        return len(self._nodes)