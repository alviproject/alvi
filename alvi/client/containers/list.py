from . import base


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container, parent, value)
        self._next = None

    @property
    def next(self):
        return self._next

    def create_child(self, value):
        self._next = Node(self._container, self, value)
        return self._next


class List(base.Container):
    @property
    def head(self):
        try:
            return self._head
        except AttributeError:
            return None

    def create_head(self, value):
        if self.head:
            raise RuntimeError("Cannot set head more that once")
        self._head = Node(self, None, value)
        return self._head