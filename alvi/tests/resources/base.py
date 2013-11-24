import abc


class ResourceFactory(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def create(*args, **kwargs):
        raise NotImplementedError()


class Resource(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def destroy(self):
        raise NotImplementedError()