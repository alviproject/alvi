import unittest
import inspect
import alvi.client.scenes as scenes
from alvi.client.api import Pipe
from mock import MagicMock
import logging


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
        container_class = scene.container_class()
        container = container_class(self.pipe)
        scene_instance = scene()
        form = scene_instance.Form()
        #intentionaly convert field.value() to str to make sure it behaves in the same way as in production
        # (when options are being sent through all layers of the system
        options = dict(((field.name, str(field.value())) for field in form))
        scene_instance.run(container, options)
        #TODO implement test for all existing scenes
        scene_instance.test(container, self)