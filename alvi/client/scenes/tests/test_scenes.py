import logging
logging.basicConfig(level=logging.INFO)
import unittest
import inspect
import alvi.client.scenes as scenes
from alvi.client.api import Pipe
from mock import MagicMock
from alvi.client.data_generators import RandomDataGenerator


logger = logging.getLogger(__name__)


class TestDefaultScene(unittest.TestCase):
    def setUp(self):
        self.pipe = Pipe("test_scene")
        self.pipe.send = MagicMock()
        self.pipe.sync = MagicMock()

    def test_scenes(self):
        for _, scene in inspect.getmembers(scenes, inspect.isclass):
            #TODO every scene shall be tested in separate test case
            self.scene_test(scene)

    def scene_test(self, scene):
        logger.info(scene)

        logger.debug("instantiating scene class")
        container_class = scene.container_class()
        container = container_class(self.pipe)
        scene_instance = scene()

        logger.debug("initializing default options")
        form = scene_instance.Form()
        options = dict(((field.name, field.value()) for field in form))

        logger.debug("creating data generator")
        data_generator_form = RandomDataGenerator.Form()
        data_generator_options = dict(((field.name, field.value()) for field in data_generator_form))
        data_generator = RandomDataGenerator(data_generator_options)

        logger.debug("running the scene")
        scene_instance.run(container=container, options=options, data_generator=data_generator)
        #TODO implement test for all existing scenes

        logger.debug("performing the test")
        scene_instance.test(container, self)