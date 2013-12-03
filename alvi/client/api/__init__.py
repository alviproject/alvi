"""
low level API
consider using higher level containers package instead this one
"""
import multiprocessing
import collections
from django.conf import settings
import time
import abc
import inspect

from .. import utils


class SubsequenceIDGenerator:
    """
    generates deterministic (in particular subsequent) IDs for subsequent objects
    """
    def __init__(self):
        self._cache = dict()

    def __call__(self, obj):
        return self._cache.setdefault(id(obj), len(self._cache))


class Pipe:
    def __init__(self, scene_instance_id, id_generator=None):
        self._scene_instance_id = scene_instance_id
        self._backlog = collections.OrderedDict()
        self._id_generator = id_generator if id_generator else SubsequenceIDGenerator()

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
        self._backlog = self._backlog.__class__()  # python 3.2 does not support clear() on dicts
        time.sleep(1)

    def generate_id(self, obj):
        return self._id_generator(obj)


class BaseScene(metaclass=abc.ABCMeta):
    @classmethod
    def start(cls):
        while True:
            #TODO send this data just once
            post_data = dict(
                name=cls.__name__,
                container=cls.container_name(),
                source=inspect.getsource(cls),
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
    def run(self, pipe):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def container_name(cls):
        raise NotImplementedError
