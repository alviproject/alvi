import inspect

from .booble import Booble
from .selection_sort import SelectionSort
from .insertion_sort import InsertionSort
from .shell_sort import ShellSort
from .merge_sort import MergeSort
from .create_tree import CreateTree
from .binary_search_tree import BinarySearchTree
from .binary_search import BinarySearch
from .linear_search import LinearSearch
from .create_graph import CreateGraph
from .base import Scene


def register(scene):
    scenes.append(scene)


def make_scene(name, function, Container):
    class SceneWrapper(Scene):
        def name(self):
            return name

        def run(self, container):
            return function(container)

        def container_class(self):
            return Container

        def source(self):
            return inspect.getsource(function)

    return SceneWrapper()


scenes = []