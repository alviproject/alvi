from . import base


class Element(base.Node):
    def __init__(self, container):
        super().__init__(container)
        self._value = 0
        self._container._pipe.send('create_element', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        self._container._pipe.send('update_element', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))


class Marker(base.Marker):
    def __init__(self, name, node):
        super().__init__(name, node)
        self._container = node._container

    def move(self, index):
        element = self._container._elements[index]
        return super().move(element)


#TODO iterators, etc
class Array(base.Container):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._elements = []

    def init(self, size):
        if self._elements:
            raise RuntimeError("Array was already initialized")
        for i in range(size):
            self._elements.append(Element(self))

    def __getitem__(self, index):
        return self._elements[index].value

    def __setitem__(self, index, value):
        self._elements[index].value = value

    def size(self):
        return len(self._elements)

    def create_marker(self, name, element_id):
        element = self._elements[element_id]
        return Marker(name, element)