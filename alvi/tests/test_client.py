import time
import logging
import importlib
import os
import unittest
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from alvi import service
import alvi.tests.pages as pages


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
        time.sleep(1)  # TODO

    @classmethod
    def _setup_client(cls):
        logger.info("setting up clients")
        cls._clients = []

        scenes = (
            'alvi.tests.scenes.graph.create_node.GraphCreateNode',
            'alvi.tests.scenes.graph.update_node.GraphUpdateNode',
            'alvi.tests.scenes.graph.remove_node.GraphRemoveNode',
            'alvi.tests.scenes.graph.add_multi_marker.GraphAddMultiMarker',
        )
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
        os.system("killall chromium-browser")  # TODO
        logger.info("setting up browser")
        #TODO config
        cls._browser = webdriver.Firefox()
        #cls._browser = webdriver.Chrome()

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
        cls._browser.quit()  # TODO config

    def test_check_scenes(self):
        home_page = pages.Home(self._browser)
        home_page.goto()
        scene_links = home_page.scene_links

        self.assertEqual(len(self._clients),
                         len(scene_links),
                         "not all client processes (scenes) were successfully connected")

    def test_create_node(self):
        graph_page = pages.Graph(self._browser, "GraphCreateNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        self.assertEqual(4, len(graph_page.svg.nodes), "create_node does not work properly")
        self.assertEqual(4, len(graph_page.svg.edges), "create_edge does not work properly")

        node_values = [int(element.find_element(By.CSS_SELECTOR, "text").text) for element in graph_page.svg.nodes]
        node_values.sort()
        created = node_values[:3]
        self.assertEqual([0, 1, 2], created, "create_node does not work properly")

    def test_update_node(self):
        graph_page = pages.Graph(self._browser, "GraphUpdateNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        updated = list(graph_page.svg.node_values)[3]
        self.assertEqual(10, updated, "update_node does not work properly")

    def test_remove_node(self):
        graph_page = pages.Graph(self._browser, "GraphRemoveNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        self.assertEqual(3, len(graph_page.svg.nodes), "remove_node does not work properly")
        node_values = list(graph_page.svg.node_values)
        node_values.sort()
        self.assertEqual([0, 1, 2], node_values, "remove_node does not work properly")

    def test_add_multi_marker(self):
        graph_page = pages.Graph(self._browser, "GraphAddMultiMarker")
        graph_page.goto()
        graph_page.wait_to_finish()

        marker = [e for e in graph_page.svg.nodes if e.find_element(By.CSS_SELECTOR, "text").text == "multi marker"]
        self.assertEquals(1, len(marker), "multi_marker was not created successfully")

        #marked node have different color
        marker = marker[0]
        color = marker.value_of_css_property("stroke")
        colors = map(lambda e: e.value_of_css_property("stroke"), graph_page.svg.nodes)
        marked = [c for c in colors if c == color]

        #expect 2 marked nodes + 1 node of multi_marker itself
        self.assertEquals(3, len(marked), "nodes were not successfully added to multi_marker")