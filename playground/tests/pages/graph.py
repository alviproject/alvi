from selenium.webdriver.common.by import By
from . import scene
from . import base


class Graph(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "g.node")
        edges = base.make_elements(By.CSS_SELECTOR, "line.link")

    def goto(self):
        super().goto()
        #TODO it would be a bit more elegant to base on text content (xpath should allow to do the right query)
        link = self._root.find_element(By.CSS_SELECTOR, "ul.scenes li a[href*=CreateGraph]")
        link.click()
