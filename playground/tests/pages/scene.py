from selenium.webdriver.common.by import By
from . import home
from selenium.webdriver.support.wait import WebDriverWait


class Scene(home.Home):
    """abstract scene, not to be used directly"""
    class SVG:
        """abstract SVG element, to be overloaded in inherited scenes"""
        def __init__(self, root):
            self._root = root

        @property
        def root(self):
            return self._root

    @property
    def svg(self):
        svg = self._root.find_element(By.CSS_SELECTOR, "svg")
        return self.__class__.SVG(svg)

    def wait_to_finish(self):
        """wait until algorithm scene is finished"""
        #TODO don't hardcode values
        WebDriverWait(self._root, 10, 0.1)\
            .until(lambda driver: driver.find_element(By.CSS_SELECTOR, "#state").text == "finished")