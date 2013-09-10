import abc
from .. import base


class Node(base.Node):
    @property
    def next(self):
        try:
            return self._next
        except AttributeError:
            return None

    @next.setter
    def next(self, node):
        if self.next:
            raise RuntimeError("Cannot set next node more that once")
        self._next = node

    @property
    @abc.abstractmethod
    def value(self):pass


class List(base.Container):
    @abc.abstractmethod
    def create_node(self, value):pass

    @property
    def head(self):
        try:
            return self._head
        except AttributeError:
            return None

    @head.setter
    def head(self, node):
        if self.head:
            raise RuntimeError("Cannot set head more that once")
        self._head = node