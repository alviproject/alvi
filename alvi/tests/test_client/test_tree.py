import logging
from alvi.tests.test_client.base import TestContainer
import alvi.tests.pages as pages

logger = logging.getLogger(__name__)


class TestTree(TestContainer):
    def test_create_node(self):
        page = pages.Tree(self._browser.driver, "TreeCreateNode")
        page.goto()

        self.assertEqual(4, len(page.svg.nodes), "create_node does not work properly")

        print(page.svg.node_data)
        #node_values = [d['name']int(element.find_element(By.CSS_SELECTOR, "text").text) for element in graph_page.svg.nodes]
        #node_values.sort()
        #created = node_values[:3]
        #self.assertEqual([0, 1, 2], created, "create_node does not work properly")
