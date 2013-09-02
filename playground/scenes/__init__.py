import inspect

from .booble import Booble
from .booble_cartesian import BoobleCartesian
from .create_tree import CreateTree
from .binary_search_tree import BinarySearchTree


class Pipe:
    def __init__(self, queue):
        self.queue = queue
        self._backlog = []

    def send(self, message):
        self._backlog.append(message)

    def sync(self):
        #TODO optimize data and stats (send only latest value if entry occurs multiple times)
        #message is sent asynchronously, so we need to make a copy, before clearing
        backlog = self._backlog.copy()
        self.queue.put(backlog)
        self._backlog.clear()


def register(scene_name, scene_function, Space):
    def _run(queue):
        pipe = Pipe(queue)
        space = Space(pipe)
        return scene_function(space)

    source = inspect.getsource(scene_function)

    scenes.append((scene_name, _run, Space, source))


scenes = []