import abc


def action(container_method):
    container_method._register = True
    return container_method


class Node(metaclass=abc.ABCMeta):
    def __init__(self, container):
        self.id = container._next_node_id()
        self._container = container
        container._nodes.append(self)


class ContainerMeta(abc.ABCMeta):
    def __init__(cls, name, bases, attributes):
        cls.actions = {}
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if hasattr(attr, '_register'):
                cls.actions[attr_name] = attr
        super().__init__(name, bases, attributes)


class Container(metaclass=ContainerMeta):
    def __init__(self):
        self._space = self.space_class()()

    def evaluate_action(self, action_name, **kwargs):
        return self.__class__.actions[action_name](self, **kwargs)

    #TODO do we still need this?
    def _next_node_id(self):
        return len(self._nodes)

    def sync(self):
        self._space.sync(1)  # TODO

    @property
    def stats(self):
        return self._space.stats

    #def create_marker(self, name, node):
    #    return self._space.create_marker(name, node)

    @classmethod
    def implementations(cls):
        return cls.__subclasses__()

    @classmethod
    @abc.abstractmethod
    def space_class(cls):
        raise NotImplementedError()

    @action
    def update_stats(self, name, value):
        return self._space.update_stats(name, value)
