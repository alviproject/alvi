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
        utils.post_to_server(settings.API_URL_SCENE_SYNC, data)
        self._backlog.clear()
        time.sleep(1)


def create_marker(pipe, id, name, item_id):
    pipe.send('create_marker', (id,), dict(
        id=id,
        name=name,
        item_id=item_id,
    ))


def move_marker(pipe, id, item_id):
    pipe.send('move_marker', (id,), dict(
        id=id,
        item_id=item_id,
    ))


def remove_marker(pipe, id):
    pipe.send('remove_marker', (id,), dict(
        id=id,
    ))


def update_stats(pipe, name, value):
    pipe.send("update_stats", (name, ), dict(
        name=name,
        value=value
    ))


def create_node(pipe, id, parent_id, value):
    pipe.send('create_node', (id, ), dict(
        id=id,
        parent_id=parent_id,
        value=value,
    ))


def update_node(pipe, id, value):
    pipe.send('update_node', (id, ), dict(
        id=id,
        value=value,
    ))

