from ..api import marker
from ..api import stats
from ..api import node
from .. import api


class Marker:
    def __init__(self, name, item):
        self._container = item._container
        marker.create(self._container._pipe, self.id, name, item.id)

    @property
    def id(self):
        return id(self)

    def move(self, item):
        marker.move(self._container._pipe, self.id, item.id)

    def remove(self):
        marker.remove(self._container._pipe, self.id)


class Stats:
    def __init__(self, pipe):
        object.__setattr__(self, '_pipe', pipe)

    def __setattr__(self, name, value):
        stats.update(self._pipe, name, value)
        return object.__setattr__(self, name, value)


class Item:
    def __init__(self, container):
        self._container = container

    @property
    def id(self):
        return id(self)


class Node(Item):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._value = value
        parent_id = parent.id if parent else 0
        node.create(self._container._pipe, self.id, parent_id, value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        node.update(self._container._pipe, self.id, v)


class Container:
    def __init__(self, scene_instance_id):
        self._pipe = api.Pipe(scene_instance_id)
        self.stats = Stats(self._pipe)

    def sync(self):
        self._pipe.sync()

    def create_marker(self, name, item):
        return Marker(name, item)

    @classmethod
    def name(cls):
        return cls.__name__