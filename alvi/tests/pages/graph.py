from selenium.webdriver.common.by import By
from . import scene
from . import base


class Graph(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "g.node")
        markers = base.make_elements(By.CSS_SELECTOR, "g.marker")
        edges = base.make_elements(By.CSS_SELECTOR, "line.link")

        @property
        def node_values(self):
            #TODO use make_element, or remove that function
            return (int(element.find_element(By.CSS_SELECTOR, "text").text) for element in self.nodes)
