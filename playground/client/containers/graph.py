from . import base
import playground.spaces


class Node(base.Node):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._value = value
        self.parent = parent
        parent_id = parent.id if parent else 0
        self._container._pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            parent_id=parent_id,
            value=self.value,
        ))

    @property
    def value(self):
        return self._value

    def create_child(self, value):
        return Node(self._container, self, value)


class Graph(base.Container):
    def create_node(self, value):
        return Node(self, None, value)