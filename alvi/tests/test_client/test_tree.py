import logging
from alvi.tests.test_client.base import TestContainer
import alvi.tests.pages as pages

logger = logging.getLogger(__name__)


class TestTree(TestContainer):
    def test_create_node(self):
        page = pages.Tree(self._browser.driver, "TreeCreateNode")
        page.goto()

        self.assertEqual(7, len(page.svg.nodes), "create_node does not work properly")

        node_data = sorted(page.svg.node_data, key=lambda d: d['id'])
        expected = [
            {'name': 0, 'id': 0, 'parent': 0},
            {'name': 1, 'id': 1, 'parent': 0},
            {'name': 2, 'id': 2, 'parent': 0},
            {'name': 3, 'id': 3, 'parent': 1},
            {'name': 4, 'id': 4, 'parent': 1},
            {'name': 5, 'id': 5, 'parent': 4},
            {'name': 6, 'id': 6, 'parent': 4}
        ]
        self.assertEqual(expected, node_data, "create_node does not work properly")

    def test_change_parent(self):
        page = pages.Tree(self._browser.driver, "TreeChangeParent")
        page.goto()

        self.assertEqual(7, len(page.svg.nodes), "create_node does not work properly")

        node_data = sorted(page.svg.node_data, key=lambda d: d['id'])
        expected = [
            {'id': 0, 'parent': 0, 'name': 0},
            {'id': 1, 'parent': 0, 'name': 1},
            {'id': 2, 'parent': 0, 'name': 2},
            {'id': 3, 'parent': 2, 'name': 3},
            {'id': 4, 'parent': 2, 'name': 4},
            {'id': 5, 'parent': 2, 'name': 5},
            {'id': 6, 'parent': 4, 'name': 6}
        ]

        self.assertEqual(expected, node_data, "change_parent does not work properly")

    def test_marker(self):
        page = pages.Tree(self._browser.driver, "TreeMarker")
        page.goto()

        self.assertEqual(7, len(page.svg.nodes), "create_node does not work properly")
        self.assertEqual(2, len(page.svg.markers), "create_marker does not work properly")

        marker0_color = page.svg.markers[0].value_of_css_property('fill')
        marker1_color = page.svg.markers[1].value_of_css_property('fill')

        marked = [n for n in page.svg.nodes if n.value_of_css_property('fill') == marker0_color]
        self.assertEquals(len(marked), 1, "create_marker does not work properly")

        marked = [n for n in page.svg.nodes if n.value_of_css_property('fill') == marker1_color]
        self.assertEquals(len(marked), 1, "create_marker or move_marker does not work properly")

    def test_multi_marker(self):
        page = pages.Tree(self._browser.driver, "TreeMultiMarker")
        page.goto()

        self.assertEqual(7, len(page.svg.nodes), "create_node does not work properly")
        self.assertEqual(1, len(page.svg.markers), "create_multi_marker does not work properly")

        marker_color = page.svg.markers[0].value_of_css_property('fill')
        marked = [n for n in page.svg.nodes if n.value_of_css_property('fill') == marker_color]
        self.assertEquals(len(marked), 2, "multi_marker_append or multi_marker_remove does not work properly")
