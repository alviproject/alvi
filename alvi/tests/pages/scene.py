from selenium.webdriver.common.by import By
from . import home
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions


class Scene(home.Home):
    SCENE_TIMEOUT = 10
    """abstract scene, not to be used directly"""
    class SVG:
        """abstract SVG element, to be overloaded in inherited scenes"""
        def __init__(self, root):
            self._root = root

        @property
        def root(self):
            return self._root

    def __init__(self, root, scene_name):
        self._scene_name = scene_name
        super().__init__(root)

    @property
    def svg(self):
        svg = self._root.find_element(By.CSS_SELECTOR, "svg")
        return self.__class__.SVG(svg)

    def wait_to_finish(self):
        """wait until algorithm scene is finished"""
        #TODO don't hardcode values
        WebDriverWait(self._root, self.SCENE_TIMEOUT, 0.1)\
            .until(lambda driver: driver.find_element(By.CSS_SELECTOR, "#state").text == "finished")

    def goto(self):
        super().goto()
        try:
            link = self._root.find_element(By.CSS_SELECTOR, "ul.scenes li a[href*=%s]" % self._scene_name)
        except selenium.common.exceptions.NoSuchElementException:
            raise RuntimeError("Scene %s cannot be found" % self._scene_name)

        link.click()

        start_scene = self._root.find_element(By.CSS_SELECTOR, "button#start_scene")
        start_scene.click()
        self.wait_to_finish()
