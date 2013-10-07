import time
import logging
import importlib
import os
import unittest
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from playground import service
import playground.tests.pages as pages


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


class TestContainer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._setup_backend()
        cls._setup_client()
        cls._setup_browser()

    @classmethod
    def tearDownClass(cls):
        cls._teardown_browser()
        cls._teardown_client()
        cls._teardown_backend()

    @classmethod
    def _setup_backend(cls):
        logger.info("setting up backend")
        config_path = os.path.join(os.path.dirname(__file__), "config.py")
        cls._backend = multiprocessing.Process(target=service.run, args=(config_path, ))
        cls._backend.start()

    @classmethod
    def _setup_client(cls):
        logger.info("setting up clients")
        scenes = ('playground.tests.scenes.graph.Graph', )
        cls._clients = []
        for scene in scenes:
            module_name, class_name = scene.rsplit(".", 1)
            module = importlib.import_module(module_name)
            class_ = getattr(module, class_name)
            process = multiprocessing.Process(target=class_.start)
            cls._clients.append(process)
            process.start()

    @classmethod
    def _setup_browser(cls):
        logger.info("setting up browser")
        #TODO config
        #cls._browser = webdriver.Firefox()
        cls._browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')

    @classmethod
    def _teardown_backend(cls):
        logger.info("terminating backend")
        cls._backend.terminate()

    @classmethod
    def _teardown_client(cls):
        logger.info("terminating client")
        for client in cls._clients:
            client.terminate()

    @classmethod
    def _teardown_browser(cls):
        logger.info("terminating browser")
        0 and cls._browser.quit()

    def test_check_scenes(self):
        home_page = pages.Home(self._browser)
        home_page.goto()
        scene_links = home_page.scene_links

        self.assertEqual(1, len(scene_links))

    def test_graph(self):
        graph_page = pages.Graph(self._browser)
        graph_page.goto()

        time.sleep(1)  # TODO

        self.assertEqual(4, len(graph_page.svg.nodes), "node.create does not work properly")
        self.assertEqual(4, len(graph_page.svg.edges), "node.create_edge does not work properly")

        node_values = [int(element.find_element(By.CSS_SELECTOR, "text").text) for element in graph_page.svg.nodes]
        node_values.sort()
        created = node_values[:3]
        updated = node_values[3:]
        self.assertEqual([0, 1, 2], created, "node.create does not work properly")
        self.assertEqual([10], updated, "node.update does not work properly")

