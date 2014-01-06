import abc
import logging
from .. import api
from django import forms

logger = logging.getLogger(__name__)


class SceneArgs:
    def __init__(self, container, options):
        self.container = container
        self.options = options


class Scene(api.BaseScene):
    """base class for container based scenes"""
    class Form(forms.Form):
        pass

    @classmethod
    def run_wrapper(cls, scene, pipe, **kwargs):
        container = cls.container_class()(pipe)
        kwargs['container'] = container
        scene.run(**kwargs)

    @classmethod
    def container_name(cls):
        return cls.container_class().name()

    @classmethod
    @abc.abstractmethod
    def container_class(cls):
        raise NotImplementedError

    def test(self, container, test_case):
        logger.warning("skipping test for %s" % self.__class__.__name__)