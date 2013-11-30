import logging
import importlib
import multiprocessing
from alvi.tests.resources.base import Resource

logger = logging.getLogger(__name__)


class LocalPythonClient(Resource):
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
        #TODO following scenes could be autodiscovered
        PREFIX = 'alvi.tests.resources.client.local_python_client.scenes.'
        return (
            PREFIX + 'graph.create_node.GraphCreateNode',
            PREFIX + 'graph.update_node.GraphUpdateNode',
            PREFIX + 'graph.remove_node.GraphRemoveNode',
            PREFIX + 'graph.add_multi_marker.GraphAddMultiMarker',
            PREFIX + 'array.create_element.ArrayCreateElement',
            PREFIX + 'tree.create_node.TreeCreateNode',
            PREFIX + 'tree.change_parent.TreeChangeParent',
            PREFIX + 'tree.change_root.TreeChangeRoot',
        )
