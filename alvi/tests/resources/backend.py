import time
import logging
import multiprocessing
from alvi import server
from alvi.tests.resources.base import Resource

logger = logging.getLogger(__name__)


class Backend(Resource):
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


