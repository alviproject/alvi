import abc
from .. import base


class Node(base.Node):
    @property
    @abc.abstractmethod
    def value(self):
        raise NotImplementedError


class Marker(object):
    def __init__(self, array, marker):
        self._marker = marker
        self._array = array

    def __getattr__(self, name):
        return self._marker.__getattribute__(name)

    def move(self, index):
        return self._marker.move(self._array._nodes[index])


class Array(base.Container):
    @abc.abstractmethod
    def _create_node(self):
        raise NotImplementedError

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

    def create_marker(self, name, index):
        return Marker(self, super().create_marker(name, self._nodes[index]))