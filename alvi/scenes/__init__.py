import uuid

import json
from .base import Scene
from .. import containers


def register(name, container_name, request):
    scene_classes[name] = make_scene(name, container_name, request)


def make_scene(name, container_name, request):
    #TODO this wrapper does not make sens anymore
    class SceneWrapper(Scene):
        def __init__(self, _id):
            self.id = _id
            self._message_evaluator = self._evaluate_message_before_init
            self._message_backlog = []
            self._message_callback = None
            self._container = self.container_implementation()()

        @staticmethod
        def container_class():
            return getattr(containers, container_name)

        def _evaluate_message_before_init(self, message):
            self._message_backlog.append(message)

        def _evaluate_message_after_init(self, message):
            args = message['args']
            result = self._container.evaluate_action(message['type'], **args)
            self._message_callback(result)

        @staticmethod
        def create():
            scene = SceneWrapper(uuid.uuid4().hex)
            scene_instances[scene.id] = scene
            response = json.dumps({'scene_instance_id': scene.id})
            request.write(response)
            #TODO request should not be finished, it would be better to keep persistent connection
            #similarly to browser<->service
            request.finish()
            return scene

        def name(self):
            return name

        def source(self):
            pass
            #return inspect.getsource(function)

        def evaluate_message(self, message):
            self._message_evaluator(message)

        def run(self, notify_callback):
            self._message_callback = notify_callback
            self._message_evaluator = self._evaluate_message_after_init
            for message in self._message_backlog:
                self.evaluate_message(message)
            self._message_backlog = []

    return SceneWrapper


scene_classes = {}
scene_instances = {}