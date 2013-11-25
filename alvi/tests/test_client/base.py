import logging
logging.basicConfig(level=logging.INFO)

import os
import unittest
from alvi.tests.resources import Backend
from alvi.tests.resources import Browser
from alvi.tests.resources import Client

logger = logging.getLogger(__name__)


class TestContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        config_path = os.path.join(os.path.dirname(__file__), "config.py")
        cls._backend = Backend.create(config_path)
        cls._client = Client.create()
        cls._browser = Browser.create()

    @classmethod
    def tearDownClass(cls):
        #cls._browser.destroy()
        cls._client.destroy()
        cls._backend.destroy()