import abc
import re
import inspect
import collections
import abc


class Pipe:
    def __init__(self, queue):
        self.queue = queue
        self._backlog = collections.OrderedDict()

    def send(self, action_type, key, message):
        message['type'] = action_type #TODO temp workaround
        key = (action_type, ) + key
        self._backlog[repr(key)] = message

    def sync(self):
        #message is sent asynchronously, so we need to make a copy, before clearing
        backlog = list(self._backlog.values())
        self.queue.put(backlog)
        self._backlog.clear()


class Scene(metaclass=abc.ABCMeta):
    def name(self):
        name = self.__class__.__name__
        #change from camel case to space delimeted
        name = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', name)
        name = name.replace("_", " ")
        return name

    @abc.abstractmethod
    def run(self, container):
        raise NotImplementedError

    @abc.abstractmethod
    def container_class(self):
        raise NotImplementedError

    def source(self):
        return inspect.getsource(self.__class__)

    #TODO change name
    def _run(self, queue):
        pipe = Pipe(queue)
        Container = self.container_implementation()
        container = Container(pipe)
        return self.run(container)

    def container_implementation(self):
        #TODO
        return self.container_class().implementations()[0]

    def template(self):
        return self.container_implementation().space_class().template


