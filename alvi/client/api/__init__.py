"""
low level API
consider using higher level containers package instead this one
"""
import multiprocessing
import collections
import time
import abc
import inspect
import alvi.client.data_generators

from .. import utils

API_URL_SCENE_SYNC = 'api/scene/sync'
API_URL_SCENE_REGISTER = 'api/scene/register'


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
        if not self._backlog:
            return
        data = dict(
            instance_id=self._scene_instance_id,
            messages=list(self._backlog.values()),
        )
        utils.post_to_server(API_URL_SCENE_SYNC, data)
        self._backlog = self._backlog.__class__()  # python 3.2 does not support clear() on dicts
        time.sleep(1)

    def generate_id(self, obj):
        return self._id_generator(obj)


class BaseScene(metaclass=abc.ABCMeta):
    @classmethod
    def start(cls):
        while True:

            available_generators = dict(list(
                (name, generator.Form().as_p()) for name, generator in alvi.client.data_generators.generators.items()
            ))
            #TODO send this data just once
            post_data = dict(
                name=cls.__name__,
                container=cls.container_name(),
                source=inspect.getsource(cls),
                form=cls.Form().as_p(),
                available_generators=available_generators,
            )
            response = utils.post_to_server(API_URL_SCENE_REGISTER, post_data)
            scene_instance_id = response['scene_instance_id']
            options = response['options']
            q = multiprocessing.Queue()
            process = multiprocessing.Process(target=cls.create_instance, args=(q, ))
            process.start()
            q.put(scene_instance_id)
            q.put(options)

    @classmethod
    def create_instance(cls, q):
        instance_id = q.get()
        options = q.get()
        scene = cls()
        pipe = Pipe(instance_id)
        cls.run_wrapper(
            scene,
            pipe,
            options=options,
            data_generator=alvi.client.data_generators.make_data_generator(options),
        )
        pipe.send('finish', (0, ), {})
        pipe.sync()

    @classmethod
    def run_wrapper(cls, scene, pipe, **kwargs):
        scene.run(pipe, **kwargs)

    @abc.abstractmethod
    def run(self, **kwargs):
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def container_name(cls):
        raise NotImplementedError
