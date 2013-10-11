import abc
from .. import api


class Scene(api.BaseScene):
    """base class for container based scenes"""
    @classmethod
    def run_wrapper(cls, scene, pipe):
        container = cls.container_class()(pipe)
        scene.run(container)

    @classmethod
    def container_name(cls):
        return cls.container_class().name()

    @classmethod
    @abc.abstractmethod
    def container_class(cls):
        raise NotImplementedError