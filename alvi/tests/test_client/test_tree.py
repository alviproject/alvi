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

    def test_change_root(self):
        page = pages.Tree(self._browser.driver, "TreeChangeRoot")
        page.goto()

        self.assertEqual(7, len(page.svg.nodes), "create_node does not work properly")

        node_data = sorted(page.svg.node_data, key=lambda d: d['id'])
        expected = [
            {'id': 0, 'parent': 1, 'name': 0},
            {'id': 1, 'parent': 0, 'name': 1},
            {'id': 2, 'parent': 0, 'name': 2},
            {'id': 3, 'parent': 1, 'name': 3},
            {'id': 4, 'parent': 1, 'name': 4},
            {'id': 5, 'parent': 4, 'name': 5},
            {'id': 6, 'parent': 4, 'name': 6},
        ]

        self.assertEqual(expected, node_data, "change_parent does not work properly")
