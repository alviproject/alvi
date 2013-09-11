import abc
from .. import base


class Node(base.Node):
    @property
    def next(self):
        try:
            return self._next
        except AttributeError:
            return None

    @property
    @abc.abstractmethod
    def value(self):pass


class List(base.Container):
    @property
    def head(self):
        try:
            return self._head
        except AttributeError:
            return None

    @abc.abstractmethod
    def create_head(self, node):pass
