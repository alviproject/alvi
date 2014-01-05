import abc
import logging
from .. import api
from django import forms

logger = logging.getLogger(__name__)


class Scene(api.BaseScene):
    """base class for container based scenes"""
    class Form(forms.Form):
        n = forms.IntegerField(min_value=1, max_value=256, label='Elements', initial=64)

    @classmethod
    def run_wrapper(cls, scene, pipe, options):
        container = cls.container_class()(pipe)
        scene.run(container, options)

    @classmethod
    def container_name(cls):
        return cls.container_class().name()

    @classmethod
    @abc.abstractmethod
    def container_class(cls):
        raise NotImplementedError

    def test(self, container, test_case):
        logger.warning("skipping test for %s" % self.__class__.__name__)