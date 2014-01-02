import logging
import unittest
from selenium.webdriver.common.by import By
import alvi.tests.pages as pages
from alvi.tests.test_client.base import TestContainer

logger = logging.getLogger(__name__)


class TestGraph(TestContainer):
    def test_create_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphCreateNode")
        graph_page.goto()

        self.assertEqual(4, len(graph_page.svg.nodes), "create_node does not work properly")
        self.assertEqual(4, len(graph_page.svg.edges), "create_edge does not work properly")

        node_values = [int(element.find_element(By.CSS_SELECTOR, "text").text) for element in graph_page.svg.nodes]
        node_values.sort()
        created = node_values[:3]
        self.assertEqual([0, 1, 2], created, "create_node does not work properly")

    @unittest.skip("graph container does not support updating nodes at the moment")
    def test_update_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphUpdateNode")
        graph_page.goto()

        updated = list(graph_page.svg.node_values)[3]
        self.assertEqual(10, updated, "update_node does not work properly")

    @unittest.skip("graph container does not support removing nodes at the moment")
    def test_remove_node(self):
        graph_page = pages.Graph(self._browser.driver, "GraphRemoveNode")
        graph_page.goto()

        self.assertEqual(3, len(graph_page.svg.nodes), "remove_node does not work properly")
        node_values = list(graph_page.svg.node_values)
        node_values.sort()
        self.assertEqual([0, 1, 2], node_values, "remove_node does not work properly")

    def test_multi_marker(self):
        graph_page = pages.Graph(self._browser.driver, "GraphAddMultiMarker")
        graph_page.goto()

        marker = [e for e in graph_page.svg.nodes if e.find_element(By.CSS_SELECTOR, "text").text == "multi marker"]
        self.assertEquals(1, len(marker), "multi_marker was not created successfully")

        #marked node have different color
        marker = marker[0]
        color = marker.value_of_css_property("stroke")
        colors = map(lambda e: e.value_of_css_property("stroke"), graph_page.svg.nodes)
        marked = [c for c in colors if c == color]

        #expect 2 marked nodes + 1 node of multi_marker itself
        self.assertEquals(3, len(marked), "nodes were not successfully added to multi_marker")

    def test_marker(self):
        graph_page = pages.Graph(self._browser.driver, "GraphMarker")
        graph_page.goto()

        marker0 = [e for e in graph_page.svg.nodes if e.find_element(By.CSS_SELECTOR, "text").text == "marker 0"]
        marker1 = [e for e in graph_page.svg.nodes if e.find_element(By.CSS_SELECTOR, "text").text == "marker 1"]
        self.assertEquals(1, len(marker0), "marker 0 was not created successfully")
        self.assertEquals(1, len(marker0), "marker 1 was not created successfully")

        #marked node have different color
        marker = marker0[0]
        color = marker.value_of_css_property("stroke")
        colors = map(lambda e: e.value_of_css_property("stroke"), graph_page.svg.nodes)
        marked = [c for c in colors if c == color]

        #expect 1 marked nodes + 1 node of marker itself
        self.assertEquals(2, len(marked), "node was not successfully marked")
