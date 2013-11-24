import logging
logging.basicConfig(level=logging.INFO)

import os
import unittest
from selenium.webdriver.common.by import By
import alvi.tests.pages as pages
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
        cls._browser.destroy()
        cls._client.destroy()
        cls._backend.destroy()

    def test_check_scenes(self):
        home_page = pages.Home(self._browser.driver)
        home_page.goto()
        scene_links = home_page.scene_links

        self.assertEqual(len(self._client.scenes),
                         len(scene_links),
                         "not all client processes (scenes) were successfully connected")

    def test_create_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphCreateNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        self.assertEqual(4, len(graph_page.svg.nodes), "create_node does not work properly")
        self.assertEqual(4, len(graph_page.svg.edges), "create_edge does not work properly")

        node_values = [int(element.find_element(By.CSS_SELECTOR, "text").text) for element in graph_page.svg.nodes]
        node_values.sort()
        created = node_values[:3]
        self.assertEqual([0, 1, 2], created, "create_node does not work properly")

    def test_update_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphUpdateNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        updated = list(graph_page.svg.node_values)[3]
        self.assertEqual(10, updated, "update_node does not work properly")

    def test_remove_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphRemoveNode")
        graph_page.goto()
        graph_page.wait_to_finish()

        self.assertEqual(3, len(graph_page.svg.nodes), "remove_node does not work properly")
        node_values = list(graph_page.svg.node_values)
        node_values.sort()
        self.assertEqual([0, 1, 2], node_values, "remove_node does not work properly")

    def test_add_multi_marker(self):
        graph_page = pages.Graph(self._browser.driver, "GraphAddMultiMarker")
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