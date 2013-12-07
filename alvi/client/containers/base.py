import alvi.client.api.base as base
import alvi.client.api.common as common


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
    def __init__(self, container, name):
        super().__init__(container)
        common.create_multi_marker(self._container._pipe, self.id, name)
        self._nodes = set()

    def add(self, node):
        if not node in self._nodes:
            common.multi_marker_add_node(self._container._pipe, self.id, node.id)
            self._nodes.add(node)

    def __contains__(self, node):
        return node in self._nodes


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

    def create_marker(self, name, node):
        return Marker(name, node)

    def create_multi_marker(self, name):
        return MultiMarker(self, name)

    @classmethod
    def name(cls):
        return cls.__name__