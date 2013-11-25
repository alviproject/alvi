from selenium.webdriver.common.by import By
from . import scene
from . import base


class Cartesian(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "circle")

        @property
        def node_data(self):
            driver = base.get_driver_from_element(self._root)
            #generally it is preferred to base on visible data in client tests,
            #however at the moment there is no simple way to get data basing on circle that visualises this data on
            #cartesian scene, that's why we have to get this data directly from JS variables
            return driver.execute_script("return points")