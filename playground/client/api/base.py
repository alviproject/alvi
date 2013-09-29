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