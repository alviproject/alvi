from selenium.webdriver.common.by import By
from . import home
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
from selenium.webdriver.support import expected_conditions


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

    def run(self, data_generator_name="sequenced", options={}):
        self.goto()
        wait = WebDriverWait(self._root, 10)
        start_scene = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button#start_scene")))

        data_generator = Select(self._root.find_element(By.CSS_SELECTOR, "#id_generator"))
        data_generator.select_by_visible_text(data_generator_name)

        for name, value in options.items():
            element = self._root.find_element(By.CSS_SELECTOR, "form [name=%s]" % name)
            element.clear()
            element.send_keys(value)

        start_scene.click()
        self.wait_to_finish()
