from selenium.webdriver.common.by import By
from . import scene
from . import base


class Tree(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "g circle")
        #edges = base.make_elements(By.CSS_SELECTOR, "line.link")

        @property
        def node_data(self):
            driver = base.get_driver_from_element(self._root)
            script = """
var circles = d3.selectAll("svg g circle")[0];
try{
    return 3;
    return circles[0].__data__;
}catch(ex) {
    return 2;
}
return $.map(circles, function(val, i) {return val.__data__;});
"""
            return driver.execute_script(script)