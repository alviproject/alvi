"""
low level API
consider using higher level containers package instead this one
"""
import multiprocessing
import collections
from django.conf import settings
import time
import abc

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


class BaseScene(metaclass=abc.ABCMeta):
    @classmethod
    def start(cls):
        while True:
            post_data = dict(
                name=cls.__name__,
                container=cls.container_name(),
            )
            response = utils.post_to_server(settings.API_URL_SCENE_REGISTER, post_data)
            scene_instance_id = response['scene_instance_id']
            process = multiprocessing.Process(target=cls.create_instance, args=(scene_instance_id,))
            process.start()

    @classmethod
    def create_instance(cls, instance_id):
        scene = cls()
        pipe = Pipe(instance_id)
        cls.run_wrapper(scene, pipe)
        pipe.send('finish', (0, ), {})
        pipe.sync()

    @classmethod
    def run_wrapper(cls, scene, pipe):
        scene.run(pipe)

    @abc.abstractmethod
    def run(self, instance_id):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def container_name(cls):
        raise NotImplementedError
