import abc
import time
import logging
import multiprocessing
from alvi import server

logger = logging.getLogger(__name__)


class Backend(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        raise NotImplemented

    @abc.abstractmethod
    def destroy(self):
        raise NotImplemented

    @staticmethod
    def create(config_path):
        return LocalBackend(config_path)


class LocalBackend(Backend):
    def __init__(self, config_path):
        logger.info("setting up backend")
        self._process = multiprocessing.Process(target=server.run, args=(config_path, ))
        self._process.start()
        time.sleep(1)  # TODO

    def destroy(self):
        logger.info("terminating backend")
        self._process.terminate()


