import inspect

from .booble import Booble
from .booble_cartesian import BoobleCartesian
from .create_tree import CreateTree
from .binary_search_tree import BinarySearchTree


def register(scene_name, scene_function, Space):
    def _run(queue):
        space = Space(queue)
        return scene_function(space)

    source = inspect.getsource(scene_function)

    scenes.append((scene_name, _run, Space, source))


scenes = []