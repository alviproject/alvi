import logging
from alvi.tests.test_client.base import TestContainer
import alvi.tests.pages as pages


logger = logging.getLogger(__name__)


class TestScenes(TestContainer):
    def test_check_scenes(self):
        home_page = pages.Home(self._browser.driver)
        home_page.goto()
        scene_links = home_page.scene_links

        self.assertEqual(len(self._client.scenes),
                         len(scene_links),
                         "not all client processes (scenes) were successfully connected")