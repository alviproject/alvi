from . import base
from ..api import element


class Element(base.Item):
    def __init__(self, container):
        super().__init__(container)
        self._value = 0
        element.create(self._container._pipe, self.id, self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        element.update(self._container._pipe, self.id, self.value)


class Marker(base.Marker):
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