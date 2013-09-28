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
    def __init__(self, name, item):
        self._container = item._container
        self._container._pipe.send('create_marker', (self.id,), dict(
            id=self.id,
            name=name,
            item_id=item.id
        ))

    @property
    def id(self):
        return id(self)

    def move(self, item):
        self._container._pipe.send('move_marker', (self.id,), dict(
            id=self.id,
            item_id=item.id
        ))

    def remove(self):
        self._container._pipe.send('remove_marker', (self.id,), dict(
            id=self.id,
        ))


class Stats:
    def __init__(self, pipe):
        object.__setattr__(self, '_pipe', pipe)

    def __setattr__(self, name, value):
        self._pipe.send("update_stats", (name, ), dict(
            name=name,
            value=value
        ))
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
        self._container._pipe.send('create_node', (self.id, ), dict(
            id=self.id,
            parent_id=parent_id,
            value=self.value,
        ))

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


class Container:
    def __init__(self, scene_instance_id):
        self._pipe = Pipe(scene_instance_id)
        self.stats = Stats(self._pipe)

    def sync(self):
        self._pipe.sync()

    def create_marker(self, name, item):
        return Marker(name, item)

    @classmethod
    def name(cls):
        return cls.__name__