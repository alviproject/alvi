import logging
import alvi.config
alvi.config.configure()
import unittest
import inspect
import alvi.client.scenes as scenes
from alvi.client.api import Pipe
from mock import MagicMock
from alvi.client.data_generators import RandomDataGenerator
from alvi.client.data_generators import generators
from unittest_data_provider import data_provider

logger = logging.getLogger(__name__)


class TestDefaultScene(unittest.TestCase):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

    def __str__(self):
        return self.scene.__name__

    def setUp(self):
        self.pipe = Pipe("test_scene")
        self.pipe.send = MagicMock()
        self.pipe.sync = MagicMock()

    #TODO work on data_provider itself and possibly send a pull request
    @data_provider(lambda: ((generator, ) for generator in generators.values()))
    def runTest(self, generator_class):
        logger.info(self.scene)

        logger.debug("instantiating scene class")
        container_class = self.scene.container_class()
        container = container_class(self.pipe)
        scene_instance = self.scene()

        logger.debug("initializing default options")
        form = scene_instance.Form()
        options = dict(((field.name, field.value()) for field in form))

        logger.debug("creating data generator")
        data_generator_form = generator_class.Form()
        data_generator_options = dict(((field.name, field.value()) for field in data_generator_form))
        data_generator = generator_class(data_generator_options)

        logger.debug("running the scene")
        scene_instance.run(container=container, options=options, data_generator=data_generator)
        #TODO implement test for all existing scenes

        logger.debug("performing the test")
        scene_instance.test(container, self)


def load_tests(loader, tests, pattern):
    test_cases = (TestDefaultScene(scene) for _, scene in inspect.getmembers(scenes, inspect.isclass))
    return unittest.TestSuite(test_cases)