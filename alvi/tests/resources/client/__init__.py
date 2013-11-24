from alvi.tests.resources.base import ResourceFactory
from alvi.tests.resources.client.local_python_client import LocalPythonClient


class Client(ResourceFactory):
    @staticmethod
    def create():
        return LocalPythonClient()
