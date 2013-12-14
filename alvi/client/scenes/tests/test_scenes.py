import unittest
import inspect
import alvi.client.scenes as scenes
from alvi.client.api import Pipe
from mock import MagicMock


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
        container_class = scene.container_class()
        container = container_class(self.pipe)
        scene_instance = scene()
        scene_instance.run(container)
        #TODO implement test for all existing scenes
        scene_instance.test(container, self)