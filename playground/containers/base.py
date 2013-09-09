import abc


class Node(metaclass=abc.ABCMeta):
    def __init__(self, container):
        self.id = container._next_node_id()
        self._container = container #TODO node should not be container aware


class Container(metaclass=abc.ABCMeta):
    def __init__(self, pipe):
        self._space = self.__class__.space_class()(pipe)
        self._nodes = []

    def _next_node_id(self):
        return len(self._nodes)

    def sync(self):
        self._space.sync(1) #TODO

    def create_marker(self, name, node):
        return self._space.create_marker(name, node)

    @classmethod
    def implementations(cls):
        return cls.__subclasses__()

    @classmethod
    @abc.abstractmethod
    def space_class(cls):
        raise NotImplementedError()
