import collections
from django.conf import settings
import time

from .. import utils


class Pipe:
    def __init__(self, scene_instance_id):
        self._scene_instance_id = scene_instance_id
        self._backlog = collections.OrderedDict()

    def send(self, action_type, key, args):
        message = dict(
            type=action_type,
            args=args
        )
        key = (action_type, ) + key
        self._backlog[repr(key)] = message

    def sync(self):
        data = dict(
            instance_id=self._scene_instance_id,
            messages=list(self._backlog.values()),
        )
        ##message is sent asynchronously, so we need to make a copy, before clearing
        #backlog = list(self._backlog.values())
        #self.queue.put(backlog)
        utils.post_to_server(settings.API_URL_SCENE_SYNC, data)
        self._backlog.clear()
        time.sleep(1)


class Marker:
    def __init__(self, name, node):
        node._container._pipe.send('create_marker', (self.id,), dict(
            id=self.id,
            name=name,
            node_id=node.id
        ))

    @property
    def id(self):
        return id(self)

    def move(self, node):
        node._container._pipe.send('move_marker', (self.id,), dict(
            id=self.id,
            node_id=node.id
        ))


class Node:
    def __init__(self, container, value):
        self._container = container
        self._value = value
        self._container._pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))
        self._next = None

    @property
    def id(self):
        return id(self)

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

    def  create_child(self, value):
        self._next = Node(self._container, value)
        return self._next


class List:
    def __init__(self, scene_instance_id):
        self._pipe = Pipe(scene_instance_id)
        self.stats = Stats(self._pipe)

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

    def sync(self):
        self._pipe.sync()

    def create_marker(self, name, node):
        return Marker(name, node)


class Stats:
    def __init__(self, pipe):
        object.__setattr__(self, '_pipe', pipe)

    def __setattr__(self, name, value):
        self._pipe.send("update_stats", (name, ), dict(
            name=name,
            value=value
        ))
        return object.__setattr__(self, name, value)
