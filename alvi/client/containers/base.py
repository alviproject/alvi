import alvi.client.api.base as base
import alvi.client.api.common as common


class Item:
    def __init__(self, container):
        self._container = container

    @property
    def id(self):
        return self._container._pipe.generate_id(self)


class Marker(Item):
    def __init__(self, name, item):
        #TODO get container as first argument to be consistent with MM
        super().__init__(item._container)
        common.create_marker(self._container._pipe, self.id, name, item.id)

    def move(self, item):
        common.move_marker(self._container._pipe, self.id, item.id)

    def remove(self):
        common.remove_marker(self._container._pipe, self.id)


class MultiMarker(Item):
    """Non intrusive marker class"""
    def __init__(self, container, name):
        super().__init__(container)
        common.create_multi_marker(self._container._pipe, self.id, name)
        self._items = set()

    def add(self, item):
        if not item in self._items:
            common.multi_marker_add_item(self._container._pipe, self.id, item.id)
            self._items.add(item)

    def __contains__(self, item):
        return item in self._items


class Stats:
    def __init__(self, pipe):
        object.__setattr__(self, '_pipe', pipe)

    def __setattr__(self, name, value):
        common.update_stats(self._pipe, name, value)
        return object.__setattr__(self, name, value)


class Node(Item):
    def __init__(self, container, parent, value):
        super().__init__(container)
        self._value = value
        if parent:
            parent_id = parent.id
        else:
            parent_id = self.id
        base.create_node(self._container._pipe, self.id, parent_id, value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v
        base.update_node(self._container._pipe, self.id, v)


class Container:
    def __init__(self, pipe):
        self._pipe = pipe
        self.stats = Stats(self._pipe)

    def sync(self):
        self._pipe.sync()

    def create_marker(self, name, item):
        return Marker(name, item)

    def create_multi_marker(self, name):
        return MultiMarker(self, name)

    @classmethod
    def name(cls):
        return cls.__name__