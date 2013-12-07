import logging
from alvi.tests.test_client.base import TestContainer
import alvi.tests.pages as pages

logger = logging.getLogger(__name__)


class TestArray(TestContainer):
    def test_array(self):
        cartesian_page = pages.Cartesian(self._browser.driver, "ArrayCreateNode")
        cartesian_page.goto()

        self.assertEqual(4, len(cartesian_page.svg.nodes), "create_element does not work properly")

        node_values = [d['y'] for d in cartesian_page.svg.node_data]
        self.assertEqual([0, 1, 2, 3], node_values, "create_element does not work properly")

    def test_update(self):
        cartesian_page = pages.Cartesian(self._browser.driver, "ArrayUpdateNode")
        cartesian_page.goto()

        self.assertEqual(4, len(cartesian_page.svg.nodes), "create_element does not work properly")

        node_values = [d['y'] for d in cartesian_page.svg.node_data]
        self.assertEqual([0, 1, 5, 3], node_values, "update_element does not work properly")
