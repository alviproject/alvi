import abc


class Resource(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def create(*args, **kwargs):
        raise NotImplementedError()

    @abc.abstractmethod
    def destroy(self):
        raise NotImplementedError()