import logging
import importlib
import multiprocessing
from alvi.tests.resources.base import Resource

logger = logging.getLogger(__name__)


class Client(Resource):
    @staticmethod
    def create():
        return LocalPythonClient()


class LocalPythonClient(Client):
    def __init__(self):
        logger.info("setting up clients")
        self._clients = []
        for scene in self.scenes:
            module_name, class_name = scene.rsplit(".", 1)
            module = importlib.import_module(module_name)
            class_ = getattr(module, class_name)
            process = multiprocessing.Process(target=class_.start)
            process.start()
            self._clients.append(process)

    def destroy(self):
        logger.info("terminating clients")
        for client in self._clients:
            client.terminate()

    @property
    def scenes(self):
        return (
            'alvi.tests.scenes.graph.create_node.GraphCreateNode',
            'alvi.tests.scenes.graph.update_node.GraphUpdateNode',
            'alvi.tests.scenes.graph.remove_node.GraphRemoveNode',
            'alvi.tests.scenes.graph.add_multi_marker.GraphAddMultiMarker',
        )
