import abc
import logging
from .. import api

logger = logging.getLogger(__name__)


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

    def test(self, container, test_case):
        logger.warning("skipping test for %s" % self.__class__.__name__)