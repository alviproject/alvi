import unittest
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from playground import service


class TestContainer(unittest.TestCase):
    def setUp(self):
        self._setup_backend()
        self._setup_client()
        self._setup_browser()

    def tearDown(self):
        self._teardown_browser()
        self._teardown_client()
        self._teardown_backend()

    def _setup_backend(self):
        self._backend = multiprocessing.Process(target=service.run)
        self._backend.start()

    def _setup_client(self):
        pass

    def _setup_browser(self):
        self._browser = webdriver.Firefox()

    def _teardown_backend(self):
        self._backend.terminate()

    def _teardown_client(self):
        #TODO
        pass

    def _teardown_browser(self):
        self._browser.quit()

    def test_check_scenes(self):
        self._browser.get("http://localhost:8000") #TODO
        scene_links = self._browser.find_elements(By.CSS_SELECTOR, "ul.scenes li a")
        self.assertEquals(11, len(scene_links))

