from booble import Booble
from booble_cartesian import BoobleCartesian
import inspect


def register(scene):
    def _run(queue):
        space = scene.Space(queue)
        return scene.run(space)

    def name():
        return scene.__class__.__name__

    def source():
        return inspect.getsource(scene.__class__)

    scenes.append(scene)
    scene._run = _run
    scene.name = name
    scene.source = source


scenes = []