from selenium.webdriver.common.by import By
from . import scene
from . import base


class Tree(scene.Scene):
    class SVG(scene.Scene.SVG):
        nodes = base.make_elements(By.CSS_SELECTOR, "g circle")

        @property
        def node_data(self):
            driver = base.get_driver_from_element(self._root)
            script = """
var nodes = d3.selectAll("svg g circle")[0];
function mapper(val, i) {
    var data = val.__data__;
    return {
        name: data.name,
        id: data.id,
        parent: data.parent ? data.parent.id : data.id
    };
}
return $.map(nodes, mapper);
"""
            return driver.execute_script(script)