from selenium.webdriver.common.by import By
from . import scene
from . import base
import selenium.common.exceptions


class Graph(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "g.node")
        edges = base.make_elements(By.CSS_SELECTOR, "line.link")

        @property
        def node_values(self):
            #TODO use make_element, or remove that function
            return (int(element.find_element(By.CSS_SELECTOR, "text").text) for element in self.nodes)

    def __init__(self, root, scene_name):
        self._scene_name = scene_name
        super().__init__(root)

    def goto(self):
        super().goto()
        try:
            link = self._root.find_element(By.CSS_SELECTOR, "ul.scenes li a[href*=%s]" % self._scene_name)
        except selenium.common.exceptions.NoSuchElementException:
            raise RuntimeError("Scene %s cannot be found" % self._scene_name)

        link.click()
        self.wait_to_finish()
