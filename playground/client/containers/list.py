from . import base


class Node(base.Node):
    def __init__(self, container, value):
        super().__init__(container)
        self._value = value
        self._container._pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))
        self._next = None

    @property
    def next(self):
        return self._next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self._container._pipe.send('update_node', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))

    def create_child(self, value):
        self._next = Node(self._container, value)
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
        self._head = Node(self, value)
        return self._head