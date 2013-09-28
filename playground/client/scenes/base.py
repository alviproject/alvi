import abc
import multiprocessing
from django.conf import settings
import playground.client.utils


class Scene(metaclass=abc.ABCMeta):
    @classmethod
    def start(cls):
        while True:
            post_data = dict(
                name=cls.__name__,
                container=cls.container_class().name(),
            )
            response = playground.client.utils.post_to_server(settings.API_URL_SCENE_REGISTER, post_data)
            scene_instance_id = response['scene_instance_id']
            process = multiprocessing.Process(target=cls.create_instance, args=(scene_instance_id,))
            process.start()

    @classmethod
    def create_instance(cls, instance_id):
        scene = cls()
        container = cls.container_class()(instance_id)
        scene.run(container)

    @abc.abstractmethod
    def run(self, instance_id):
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def container_class():
        raise NotImplementedError