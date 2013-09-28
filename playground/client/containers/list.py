import collections
from django.conf import settings

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


class Node:
    def __init__(self, container, value):
        self._container = container
        self._value = value
        self._container._pipe.send('create_point', (self.id, ), dict(
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
        self._container._pipe.send('update_point', (self.id, ), dict(
            id=self.id,
            value=self.value,
        ))

    def  create_child(self, value):
        self._next = Node(self._container, value)
        return self._next


class List:
    def __init__(self, scene_instance_id):
        self.stats = Stats()
        self._pipe = Pipe(scene_instance_id)

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


#TODO
class Stats:
    pass