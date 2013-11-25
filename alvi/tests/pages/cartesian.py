from selenium.webdriver.common.by import By
from . import scene
from . import base


class Cartesian(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "circle")

        @property
        def node_data(self):
            driver = base.get_driver_from_element(self._root)
            #TODO use d3.selectAll("circle")XXXX.__data__
            return driver.execute_script("return points")