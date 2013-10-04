from ..api import marker
from ..api import multi_marker
from ..api import stats
from ..api import node
from .. import api


class Marker:
    def __init__(self, name, item):
        #TODO get container as first argument to be consistent with MM
        self._container = item._container
        marker.create(self._container._pipe, self.id, name, item.id)

    @property
    def id(self):
        return id(self)

    def move(self, item):
        marker.move(self._container._pipe, self.id, item.id)

    def remove(self):
        marker.remove(self._container._pipe, self.id)


class MultiMarker:
    """Non intrusive marker class"""
    def __init__(self, container, name):
        self._container = container
        multi_marker.create(self._container._pipe, self.id, name)
        self._items = set()

    @property
    def id(self):
        return id(self)

    def add(self, item):
        if not item in self._items:
            multi_marker.add(self._container._pipe, self.id, item.id)
            self._items.add(item)

    def __contains__(self, item):
        return item in self._items


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

    def create_multi_marker(self, name):
        #TODO move it to Container (same for create_marker)
        return MultiMarker(self, name)

    @classmethod
    def name(cls):
        return cls.__name__