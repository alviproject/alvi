import inspect
import collections

from .booble import Booble
from .create_tree import CreateTree
from .binary_search_tree import BinarySearchTree
from .binary_search import BinarySearch
from .linear_search import LinearSearch


class Pipe:
    def __init__(self, queue):
        self.queue = queue
        self._backlog = collections.OrderedDict()

    def send(self, action_type, key, message):
        message['type'] = action_type #TODO temp workaround
        key = (action_type, ) + key
        self._backlog[repr(key)] = message

    def sync(self):
        #TODO optimize data and stats (send only latest value if entry occurs multiple times)
        #message is sent asynchronously, so we need to make a copy, before clearing
        backlog = list(self._backlog.values())
        self.queue.put(backlog)
        self._backlog.clear()


def register(scene_name, scene_function, Container):
    #TODO
    Container = Container.implementations()[0]

    def _run(queue):
        pipe = Pipe(queue)
        container = Container(pipe)
        return scene_function(container)

    try:
        obj = scene_function.__self__.__class__
    except AttributeError:
        obj = scene_function
    source = inspect.getsource(obj)

    scenes.append((scene_name, _run, Container, source))


scenes = []