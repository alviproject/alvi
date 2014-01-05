import alvi.client.api.base as base
import alvi.client.api.common as common
from contextlib import contextmanager


class Item:
    def __init__(self, container):
        self._container = container

    @property
    def id(self):
        return self._container._pipe.generate_id(self)


class Marker(Item):
    def __init__(self, name, node):
        #TODO get container as first argument to be consistent with MM
        super().__init__(node._container)
        common.create_marker(self._container._pipe, self.id, name, node.id)

    def move(self, node):
        common.move_marker(self._container._pipe, self.id, node.id)

    def remove(self):
        common.remove_marker(self._container._pipe, self.id)


class MultiMarker(Item):
    """Non intrusive marker class"""
    def __init__(self, container, name, **kwargs):
        super().__init__(container)
        common.create_multi_marker(self._container._pipe, self.id, name, **kwargs)
        self._nodes = set()

    def append(self, node):
        if not node in self._nodes:
            common.multi_marker_append(self._container._pipe, self.id, node.id)
            self._nodes.add(node)

    def remove(self, node):
        self._nodes.remove(node)
        common.multi_marker_remove(self._container._pipe, self.id, node.id)

    def __contains__(self, node):
        return node in self._nodes

    def __len__(self):
        return len(self._nodes)


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
        self._sync_postponed = False
        self._sync_waiting = False
        self.stats = Stats(self._pipe)

    def sync(self):
        if self._sync_postponed:
            self._sync_waiting = True
        else:
            self._pipe.sync()

    @contextmanager
    def postpone_sync(self):
        self._sync_postponed = True
        yield
        self._sync_postponed = False
        if self._sync_waiting:
            self._sync_waiting = False
            self.sync()

    def create_marker(self, name, node):
        return Marker(name, node)

    def create_multi_marker(self, name, **kwargs):
        return MultiMarker(self, name, **kwargs)

    @classmethod
    def name(cls):
        return cls.__name__