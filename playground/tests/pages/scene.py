from selenium.webdriver.common.by import By
from . import home


class Scene(home.Home):
    """abstract scene, not to be used directly"""
    class SVG:
        """abstract SVG element, to be overloaded in inherited scenes"""
        def __init__(self, root):
            self._root = root

    @property
    def svg(self):
        svg = self._root.find_element(By.CSS_SELECTOR, "svg")
        return self.__class__.SVG(svg)